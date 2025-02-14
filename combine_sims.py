import pandas as pd
import matplotlib.pyplot as plt
import sys

dfs = []

step_label = 'Step' 
avg_payoff = 'Avg Payoff in Window'
results_path = 'results/'

#no_of_simulations = 6
simulations = []

ratio_string = sys.argv[1]
ratio = ratio_string.split(',')

sim_string = sys.argv[3]
sim_tokens = sim_string.split(',')
if len(sim_tokens) == 1:
    simulations = range(1, int(sim_tokens[0]) + 1)
else:
    simulations = [int(x) for x in sim_tokens]
no_of_simulations = len(simulations)

def get_ratio_part():
    return '_' + '_'.join(ratio)

if len(sys.argv) > 2 and sys.argv[2] == '2':
    suffix = get_ratio_part() + '_updated_base' + '.csv'
    scheme_suffix = '_sch2'
elif len(sys.argv) > 2 and sys.argv[2] == '3':
    suffix = get_ratio_part() + '_multi_updated_base' + '.csv'
    scheme_suffix = '_sch3'
else:
    suffix = get_ratio_part() + '.csv'
    scheme_suffix = '_sch1'

for i in range(no_of_simulations):
    #file_name = 'Results_Sim' + str(i+1) + suffix
    sim_id = simulations[i]
    file_name = results_path + 'Results_Sim' + str(sim_id) + suffix
    #file_name = 'Results_Sim' + str(i+1) + '.csv'
    print(f'Reading file = %s' % file_name)
    try:
        dfs.append(pd.read_csv(file_name))
    except:
        dfs.append(None)

dfs = [x[[step_label, avg_payoff]] if x is not None else None for x in dfs]

#labels = ['Fixed', 'Sanctioning', 'Poros', 'Rule-Based RL with default', 'Rule-Based RL without explanation', 'StateRL base greedy', 'Rule-Based RL', 'LCS OG', 'LCS Sanctioning', \
#        'LCS Epsilong exploration', 'LCS Initial Only Epsilon exploration', 'LCS Initial Only alternating exploration', \
#        'LCS', 'LCS Butz', 'LCS without explanation', 'LCS Butz with new explanation', 'LCS with explanation', \
#        'LCS Butz without explanation + own norms']
colors = ['green', 'black', 'tab:red', 'red', 'yellow', 'purple', 'aqua', 'maroon', 'cyan', 'brown', 'pink', 'gray', 'orange', 'lightcoral', 'olive', 'coral', 'tab:blue', 'blue']



label_map = {'15' : 'NSIGA', '17': 'XSIGA', '1': 'Fixed', '3': 'Poros'}
color_map = {'15' : 'tab:blue', '17': 'tab:orange', '1': 'tab:green', '3': 'tab:red'}

#title = 'Average Payoffs for ratio ' + ':'.join(ratio) +  ' (Perfect:Selfish:Generous)'

#SMALL_SIZE = 14
#MEDIUM_SIZE = 14
#BIG_SIZE = 15
#BIGGER_SIZE = 16
#
#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=BIG_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


fig, ax = plt.subplots()
#ax.set(xlabel = 'Steps', ylabel = 'Social Experience')
#fig.set_size_inches(3.5, 1.77)
#fig.set_size_inches(2.83, 1.338)
fig.set_size_inches(2.83, 1.77)
fig.set_dpi(256)
#ax.set_xlabel('Steps', fontsize = 8)
#ax.set_ylabel('Social Experience', fontsize = 8)
ax.set_xlabel('Steps', fontsize = 8)
ax.set_ylabel('Social Experience', fontsize = 8)
#plt.figure(num = fig, figsize=(3,3), dpi = 80)

for i in range(no_of_simulations):
    df = dfs[i]
    sim_id = simulations[i]
    if df is not None:
        #ax.plot(df[step_label], df[avg_payoff], color = colors[sim_id - 1], label = labels[sim_id - 1])
        #ax.plot(df[step_label], df[avg_payoff], color = colors[sim_id - 1], label = label_map[str(sim_id)])
        ax.plot(df[step_label], df[avg_payoff], color = color_map[str(sim_id)], label = label_map[str(sim_id)])

params = {'legend.fontsize': 8,
          'legend.handlelength': 0.5,
          'legend.columnspacing': 0.8,
          #'legend.labelspacing': 0.01
          }

plt.rcParams.update(params)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
#plt.legend(loc = 'lower right', prop = {'size': 7})
plt.legend(loc = 'lower center', ncol=3)
#plt.legend(loc = 'best')
str_sims = [str(x) for x in simulations]
ext = '.pdf'
#fig.savefig('SocialExperience' + get_ratio_part() + '___' + '_'.join(str_sims) + scheme_suffix + ext, dpi = 100)
plt.tight_layout()
plt.show()
