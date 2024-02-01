import pathlib
from pandas import read_csv, concat
_data_path = pathlib.Path(__file__).parent.resolve()


class _Dataset:
    def __init__(self, path: pathlib.Path, type="csv") -> None:
        self.path = path
        self.folders = list(path.glob("*/"))
        self.type = type

    def makepath(self,key):
        key = self.path /key    
        if key not in self.folders: 
            raise KeyError("data not found")
        return key
    
    def __getitem__(self, x):
        x = self.makepath(x)
        
        files = x.glob("*.{}".format(self.type)) 

        return concat((read_csv(x) for x in files))


dataset = _Dataset(_data_path / "raw")

if __name__ == "__main__":

    print(dataset.folders)

    print(dataset["cova"])
