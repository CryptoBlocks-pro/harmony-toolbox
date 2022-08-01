import os
import time
import dotenv
from os import environ
from dotenv import load_dotenv
from utils.config import validatorToolbox
from utils.installer import firstSetup, printStars, recheckVars, passphraseStatus, recoverWallet
from utils.shared import loaderIntro, setWalletEnv, askYesNo, loadVarFile
from utils.toolbox import runRegularNode, runFullNode

if __name__ == "__main__":
    os.system("clear")
    loaderIntro()
    if not os.path.exists(validatorToolbox.dotenv_file):
        firstSetup()
    loadVarFile()
    if not environ.get("VALIDATOR_WALLET"):
        recoverWallet()
        if not environ.get("VALIDATOR_WALLET"):
            print(
                "* You don't currently have a validator wallet address loaded in your .env file, please edit ~/.easynode.env and add a line with the following info:\n "
                + "* VALIDATOR_WALLET='validatorONEaddress' "
            )
            input("* Press any key to exit.")
            raise SystemExit(0)
    exec(open("./toolbox/menu.py").read())
