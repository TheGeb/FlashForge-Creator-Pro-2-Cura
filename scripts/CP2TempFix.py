import re  # To perform the search and replace.

from ..Script import Script

class CP2TempFix(Script):

    def getSettingDataString(self):
        return """{
            "name": "Creator Pro 2 Temperature Fix",
            "key": "CP2TempFix",
            "metadata": {},
            "version": 2,
            "settings": {}
        }"""

    def execute(self, data):

        #Finds matches for lines which only contain 'T#', or are M104/M109 codes without a tool specified 
        search_regex = re.compile(
            "\n(T\d)\n|\n(M10[49] S\d\d\d)\n")

        for layer_number, layer in enumerate(data):
            offset = 0
            for match in re.finditer(search_regex, layer):
                tool = str(match.group(1) or tool)
                if(match.group(2)):
                    insert = " " +  str(tool or ";UNKNOWN TOOL")
                    #Don't assume tool if not found
                    position = match.span(2)[1] + offset
                    layer = layer[:position] + insert + layer[position:]
                    offset += len(insert)

            data[layer_number] = layer
            
        return data