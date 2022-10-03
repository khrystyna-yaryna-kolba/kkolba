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
        try:
            id = Validation.validate_collection_id(self, id)
            for el in self._collection:
                if el.ID == id:
                    self._collection.remove(el)
                    self._ids.remove(el.ID)
                    return
        except KeyError as k:
            print(k, "deletion was not completed")
    def edit_by_id(self, id, prop, new_value):
        try:
            id = Validation.validate_collection_id(self, id)
            for i, el in enumerate(self._collection):
                if el.ID == id:
                    prop = Validation.validate_property(el, prop)
                    if prop == "ID":
                        self._ids.remove(el.ID)
                        new_value = Validation.validate_new_id(self, new_value)
                        self._ids.add(new_value)
                    setattr(self._collection[i], prop, new_value)
                    return
        except KeyError as k:
            print(k, "editing was not completed")
        except AttributeError as n:
            print(n, "editing was not completed")
    def sort(self, sorting_attr = "number", reverse = False):
        try:
            sorting_attr = Validation.validate_default_property(sorting_attr, Container.default_props())

            # function helper to lambda
            def get_attr(x):
                attr = getattr(x, sorting_attr)
                if isinstance(attr, str):
                    return attr.lower()
                else:
                    return attr

            self._collection = sorted(self._collection, key=lambda x: get_attr(x), reverse=reverse)
        except AttributeError as n:
            print(n, "sorting was not completed")
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
        name = Validation.validate_file_name(name, "json")
        try:
            f = open(name, encoding='utf-8')
        except FileNotFoundError as e:
            print("invalid file to read from", str(e))
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
        try:
            elem.ID = Validation.validate_new_id(self, elem.ID)
            self._collection.append(elem)
            self._ids.add(elem.ID)
        except KeyError as k:
            print(k, "Container was not added! IDs of containers in collection must be unique")




