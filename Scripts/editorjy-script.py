
# -*- coding: utf-8 -*-
import re
import sys

import editorjy
from editorjy.start import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    main()