
class dataService():

    def request_data(self, data, filter, schema):

        for k, v in filter.items():
            operator = self.get_operator_value(v)
            fieldName = self.get_field_name(k, schema)

            # Filtering data based on the operator
            if operator == "gt":
                return [d for d in data if d[fieldName] > v[operator]]
            elif operator == "lt":
                return [d for d in data if d[fieldName] < v[operator]]
            elif operator == "eq":
                return [d for d in data if d[fieldName] == v[operator]]
            elif operator == "not":
                return [d for d in data if d[fieldName] != v[operator]]
            else:
                return []


    def get_operator_value(self, dict):
        operator = ""
        for key in dict.keys():
            operator = key
        return operator

    def get_field_name(self, k, schema):
        for field in schema:
            if field["name"] == k:
                return field["display"]

    def get_station_by_id(self, id, data):
        return [d for d in data if d["id"] == id]

    def delete_station_by_id(self, id, data):
        for d in data:
            if d["id"] == id:
                data.remove(d)
                return 200