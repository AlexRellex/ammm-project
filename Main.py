import sys
from datParser import DATParser
from ValidateConfig import ValidateConfig
from InstanceGenerator import InstanceGenerator
from AMMMGlobals import AMMMException


def run():
    try:
        configFile = "configfiles/config.dat"
        print("AMMM Instance Generator")
        print("-----------------------")
        print("Reading Config file %s..." % configFile)
        config = DATParser.parse(configFile)
        print("Config file parsed...")
        ValidateConfig.validate(config)
        print("Creating Instances...")
        instGen = InstanceGenerator(config)
        instGen.generate()
        print("Done")
        return 0
    except AMMMException as e:
        print("Exception: %s", e)
        return 1
    except Exception as e:
        print("#############################")
        print("UNEXPECTED EXCEPTION HAPPENED %s", e)
        print("#############################")
        print(f"{e}")
        return 1

if __name__ == '__main__':
    sys.exit(run())
