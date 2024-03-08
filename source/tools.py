import requests
import toml

pallete = ["#8fa5e3", "#9285cc","#5C6BC0","#5d55d5", "#533eab", "#4929cf", "#2b2640", "#8c74f2"]

def updateTOML(e=None, parent=None, child=None, parameter=None):
    config = toml.load(r'.\data\config.toml')
    config[parent][child][parameter] = e.path
    f = open(r'.\data\config.toml','w')
    toml.dump(config, f)
    f.close()