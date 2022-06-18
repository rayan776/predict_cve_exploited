"""Initialize logging, global variables.

setup_logging: Initialize logging

init_globals: Initialize global variables

"""
import os
import json
import logging.config
import io
import zipfile as zipf
import requests


def get_zip(my_url) -> tuple:
    """Download and unzip a file

    This utility rtn downloads a file given the URL and then unzips it.

    Returns
    =======
    (file_name, extracted_file)
            Filename    Name in file in the zip archive
            extracted_file
                        Contents of file

            (None, None) is returned if an error is detected.

    Exceptions
    ==========
    RequestException:   The requests module, used for https access, has
                    several exception conditions.

    Restrictions
    ============

    This rtn is designed to be used for NIST XML file downloads.
    The assumption is that the archive contains only 1 XML in zipped format.
    The contents of the file are read into memory.

    I/P Parameters
    ==============

    :param my_url:   The URL of the file to be downloaded
    """
    print('\n\nEntering get_zip to read {0}\n\n'.format(my_url))

    try:
        resp = requests.get(my_url)

    except requests.exceptions.RequestException as e:
        print('\n\n***NVD XML feeds - Error: \n{0}\n{0}\n\n'.format(my_url, e))
        return None, None

    # unzip compressed archive
    my_zipfile = zipf.ZipFile(io.BytesIO(resp.content))

    zip_names = my_zipfile.namelist()

    # should be only 1 file in the archive
    if len(zip_names) == 1:
        file_name = zip_names.pop()
        extracted_file = my_zipfile.read(file_name)
        print(extracted_file.__sizeof__())
        print('get_zip: Successfully extracted {0}'.format(file_name))
        return file_name, extracted_file
    else:
        print('get_zip: Error in extracting NVD zip file')
        return None, None
