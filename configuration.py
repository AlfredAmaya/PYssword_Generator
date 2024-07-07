from dataclasses import dataclass
import dataclass_wizard 

@dataclass
class configuration(dataclass_wizard.JSONListWizard,str=False) :
    size:int
    lower:str
    upper:str
    special:str
    number:str

 