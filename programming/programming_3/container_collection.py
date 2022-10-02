from container import Container
from validation import Validation
import json
class ContainerCollection:
    def __init__(self, *values):
        self._collection = list(values[:])
        self._ids = set()
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
    def delete_by_id(self, id):
        if not id in self._ids:
            print("container with such id does not exist")
            return
        for el in self._collection:
            if el.ID == id:
                self._collection.remove(el)
                self._ids.remove(el.ID)
                return
    def edit_by_id(self, id, prop, new_value):
        if not Validation.if_id_exist(self, id):
            print("container with such id does not exist")
            return
        if not prop in Container.default_props():
            print("invalid attribute, editing was not done")
            return
        for i, el in enumerate(self._collection):
            if el.ID == id:
                if prop == "ID":
                    self._ids.remove(el.ID)
                    self._ids.add(id)
                setattr(self._collection[i], prop, new_value)
                return
    def sort(self, sorting_attr = "number", reverse = False):
        if not sorting_attr in Container.default_props():
            print("invalid sorting attribute, sorting was not done")
            return
        def get_attr(x):
            attr = getattr(x, sorting_attr)
            if type(attr)=="str":
                return attr.lower()
            else:
                return attr
        self._collection = sorted(self._collection, key= lambda x: get_attr(x), reverse= reverse)
    def write_to_txt_file(self, name):
        name = Validation.validate_file_name(name, "txt")
        f = open(name, mode='w', encoding='utf-8')
        for cont in self._collection:
            f.write(cont.__str__())
            f.write("\n")
        f.close()
    def write_to_json_file(self, name):
        name = Validation.validate_file_name(name, "json")
        res = []
        for i in self._collection:
            res.append(i.props())
        with open(name, "w") as f:
            json.dump(res, f, indent=4)
        f.close()
    def read_json_file(self, name):
        Validation.validate_file_name(name, "json")
        try:
            f = open(name, encoding='utf-8')
        except FileNotFoundError as e:
            print(str(e))
            return
        self._collection = []
        self._ids.clear()
        file = json.load(f)
        for i, container in enumerate(file):
            try:
                self.add_element(Container(**container))
            except ValueError as e:
                print(str(e), "in {} object in file".format(i))
                continue
        f.close()
    def add_element(self, elem):
        if Validation.if_id_exist(self, elem.ID):
            print("Container was not added! IDs of containers in collection must be unique")
            return
        self._collection.append(elem)
        self._ids.add(elem.ID)




