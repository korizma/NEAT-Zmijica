"""
Zmijica
"""

import os
import statistics
import pickle
import zmijica
import neat
import igrica_nn as play
import math
import visualize

max_ftns = 0
generacija = 0
test = 91

def sacuvaj_genom(genome, filename):
    f = open(filename, 'w')
    f.close()


    file = open(filename, "wb")
    pickle.dump(genome, file)
    file.close()


def analiziraj_outpute(out):
    max = 0
    for k in out:
        if k > max:
            max = k
    index = out.index(max)
    return index+1

def odigraj_partiju(genome, config, jabuka_seed):
    igra = zmijica.Igra()
    net = neat.nn.RecurrentNetwork.create(genome, config)
    igra.nova_igra()
    igra.jabuka_seed = jabuka_seed
    inputs = igra.prebaci_u_niz()
    outputs = net.activate(inputs)
    smer = analiziraj_outpute(outputs)

    while igra.pomeri_zmiju(smer) and igra.broj_poteza < 40 and igra.uk_broj_poteza < 16*64:
        inputs = igra.prebaci_u_niz()
        outputs = net.activate(inputs)
        smer = analiziraj_outpute(outputs)

    score = len(igra.zmija)
    return score-2

def eval_genomes(genomes, config):
    global max_ftns, test, generacija
    igra = zmijica.Igra()
    pom = 0
    pom_max = 0
    id_max = -1
    for genome_id, genome in genomes:

        genome.fitness = odigraj_partiju(genome, config, test)
        
        if genome.fitness > pom_max:
            pom_max = genome.fitness
            id_max = genome
        if math.floor(genome.fitness) > max_ftns:
            sacuvaj_genom(genome, "Bolji/boljiFitness_"+str(math.floor(max_ftns))+".pckl")
            max_ftns = math.floor(genome.fitness)
    sacuvaj_genom(id_max, 'generacije/best_gen'+str(generacija)+".pckl")
    generacija += 1
    return

def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)
    sacuvaj_genom(winner, "pobenik.pckl")
    # Display the winning genome.
    najbolji = stats.best_genomes(101)
    for i in range(100):
        strng = str(i)+"tiGenom.pckl"
        sacuvaj_genom(najbolji[i], strng)

    visualize.plot_stats(stats, ylog=False)
    visualize.plot_species(stats)

    stdev_po_generaciji = stats.get_fitness_stdev()
    medijana_po_generaciji = stats.get_fitness_median()
    prosek_po_generaciji = stats.get_fitness_mean()

    velicina_speciesa = stats.get_species_sizes()
    fitness_speciesa = stats.get_species_fitness(null_value='0')


    sacuvaj_genom(stdev_po_generaciji, "podaci/stdev_po_gen.pckl")
    sacuvaj_genom(medijana_po_generaciji, "podaci/medij_po_gen.pckl")
    sacuvaj_genom(prosek_po_generaciji, "podaci/prosek_po_gen.pckl")

    sacuvaj_genom(velicina_speciesa, "podaci/vel_spec.pckl")
    sacuvaj_genom(fitness_speciesa, "podaci/fit_spec.pckl")


    sacuvaj_genom(stats, "podaci/statistika.pckl")

    # visualize.plot_stats(stats, ylog=False, view=True)
    #
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    # p.run(eval_genomes, 10)
    #
    # fitness
    # plot
    # svih
    # generacija
    # species
    # plot
    # stdev
    # po
    # generaciji
    # medijana
    # fitnesa
    # po
    # generaciji
    # prosek
    # fitnesa
    # po
    # generaciji
    # velicine
    # species - a, njihovi
    # fitnesi
    #
    # izgled
    # neuronskih
    # prvih
    # 100
    # izgled
    # neuronskih
    # najbolje
    # jedinke
    # svake
    # generacije


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)