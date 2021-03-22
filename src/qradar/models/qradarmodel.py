class QRadarModel:
    @classmethod
    def from_json(cls, json):
        if isinstance(json, list) and len(json) == 1:
            obj = cls()
            for att in vars(obj):
                if att is not None:
                    setattr(obj, att, json[0].get(att, None))
            return obj
        if isinstance(json, list):
            listofitems = []
            for item in json:
                obj = cls()
                for att in vars(obj):
                    if att is not None:
                        setattr(obj, att, item.get(att, None))
                listofitems.append(obj)
            return listofitems
        else:
            raise ValueError

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
