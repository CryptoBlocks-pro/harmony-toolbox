import os
import dotenv
from os import environ
from toolbox.config import easy_env
from toolbox.library import loaderIntro, setWalletEnv, askYesNo, printStars, recoverWallet

if __name__ == "__main__":
    os.system("clear")
    loaderIntro()
    print(
        "* Harmony ONE Validator Wallet Import"
    )
    printStars()
    question = askYesNo(
            "\n* You will directly utilize the harmony application interface"
            + "\n* We do not store any pass phrases  or data inside of our application"
            + "\n* Respond yes to recover your validator wallet via Mnemonic phrase now or say NO to create a new wallet post-install"
            + "\n* Restore an existing wallet now? (YES/NO) "
        )
    if question:
        dotenv.unset_key(easy_env.dotenv_file, "VALIDATOR_WALLET")
        dotenv.unset_key(easy_env.dotenv_file, "PASS_SWITCH")
        dotenv.unset_key(easy_env.dotenv_file, "NODE_WALLET")
        recoverWallet()
        setWalletEnv()
