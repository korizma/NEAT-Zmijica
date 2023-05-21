import neat
import pickle
import igrica_nn
import os
import zmijica

local_dir = os.path.dirname(__file__)
config_file = os.path.join(local_dir, 'config')

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

f = open("Bolji/boljiFitness_5.pckl", "rb")
genom = pickle.load(f)
f.close()
igrica_nn.play_game(genom, config)



#
# f = open('fit_spec.pckl', 'rb')
# pe = pickle.load(f)
# f.close()
# print(pe)