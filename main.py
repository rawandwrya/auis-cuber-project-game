from hangman import start
from phoenix import main as phoenix
from mo import mo
from zhsha import main as zhsha
from ring import main as ring
from throne import main as throne
from sword import sword
from koagame import main as koagame



game_path = start.starting_hangman()

if game_path == 'phoenix':
    phoenix.phoenix()
elif game_path == 'unknown':
    mo.unknown()
elif game_path == 'tradition':
    zhsha.tradition()
elif game_path == 'ring':
    ring.ring()
elif game_path == 'throne':
    throne.throne()
elif game_path == 'sword':
    sword.introduction()
elif game_path == 'hope':
    koagame.hope()
