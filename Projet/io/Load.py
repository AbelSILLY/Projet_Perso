import os
import pandas as pd
import pooch
from Projet.io import url_db, path_target
import lzma


class Load_db:
    """
    This class download the weather dataset.

    Parameters:
    -----------

    url : (string) path to the data
    target_name : (string) local path where data is saved
    """

    def __init__(self, url=url_db, target_name=path_target):
        path, fname_compressed = os.path.split(path_target)
        self.fname=path +"/"+fname_compressed
        pooch.retrieve(url, path=path, fname=fname_compressed, known_hash=None)
   #     self.fname = self.unxz(path_target)

    def unxz(self, fname_compressed):
        fname_uncompressed = fname_compressed[:-3]

        # do nothing if uncompressed file exists
        if os.path.exists(fname_uncompressed):
            return fname_uncompressed

        # read the compressed file
        with lzma.open(fname_compressed) as f:
            file_content = f.read().decode('utf-8')

            # write the string file_content to a file named fname_uncompressed
            with open(fname_uncompressed, 'w') as f:
                f.write(file_content)

        return fname_uncompressed

    def save_as_df(self):
        df_weather = pd.read_csv(
            self.fname,
            na_values="",
            low_memory=False,
           # converters={"data": str, "heure": str},
            encoding="latin-1",
            skiprows=[0,1,2]
        )
        return df_weather