import sys 
sys.path.append('C:\\Users\\Ghassen\\Desktop\\CEXDEXBOT\\whack-a-mole')

import asyncio

from strategies.dex_arb_base import main


if __name__ == '__main__':
    asyncio.run(main())
