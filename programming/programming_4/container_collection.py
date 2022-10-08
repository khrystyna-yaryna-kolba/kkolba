from container import Container
from validation import Validation
import json
class ContainerCollection:
    def __init__(self, *values):
        self._collection = []
        self._ids = set()
        for val in values:
            try:
                self.add_element(val)
            except KeyError as k:
                print(k)
            except ValueError as v:
                print(v)

    def search(self, elem):
        found = ContainerCollection()
        for x in self._collection:
            for i in x.__dict__.values():
                if str(i).find(elem)!=-1:
                    found.add_element(x)
                    break
        return found

    def __getitem__(self, item):
        return self._collection[item]

    def get_ids(self):
        return self._ids

    def __str__(self):
        return "\n".join([i.__str__() for i in self._collection])

    @Validation.validate_collection_id
    def delete_by_id(self, id):
        for el in self._collection:
            if el.ID == id:
                self._collection.remove(el)
                self._ids.remove(el.ID)
                return


    # helper, cuz editing id has a bit different logic
    @Validation.validate_edit_id
    def edit_id(self, new_val, el):
        d = el.ID
        setattr(el, "ID", new_val)
        self._ids.remove(d)
        self._ids.add(new_val)

    @Validation.validate_collection_id
    @Validation.validate_default_property(Container.default_props(), 2)
    def edit_by_id(self, id, prop, new_value):
        for i, el in enumerate(self._collection):
            if el.ID == id:
                if prop == "ID" and id!=new_value:
                    self.edit_id( new_value, el)
                    return
                setattr(self._collection[i], prop, new_value)
                return



    @Validation.validate_default_property(Container.default_props(), 1)
    def sort(self, sorting_attr = "number", reverse = False):
        # function helper to lambda
        def get_attr(x):
            attr = getattr(x, sorting_attr)
            if isinstance(attr, str):
                return attr.lower()
            else:
                return attr
        self._collection = sorted(self._collection, key=lambda x: get_attr(x), reverse=reverse)



    @Validation.validate_file_name("txt")
    def write_to_txt_file(self, name):
        f = open(name, mode='w', encoding='utf-8')
        for cont in self._collection:
            f.write(cont.__str__())
            f.write("\n")
        f.close()



    @Validation.validate_file_name("json")
    def write_to_json_file(self, name):
        res = []
        for i in self._collection:
            res.append(i.props())
        with open(name, "w") as f:
            json.dump(res, f, indent=4)
        f.close()



    @Validation.validate_file_name("json")
    @Validation.validate_existing_file
    def read_json_file(self, f):
        self._collection = []
        self._ids.clear()
        file = json.load(f)
        for i, container in enumerate(file):
            try:
                self.add_element(Container(**container))
            except ValueError as e:
                print(str(e), "\nin {} object in file".format(i))
                continue
            except KeyError as k:
                print(k, "Container was not added! IDs of containers in collection must be unique")
        f.close()



    @Validation.validate_new_id
    def add_element(self, elem):
        self._collection.append(elem)
        self._ids.add(elem.ID)


