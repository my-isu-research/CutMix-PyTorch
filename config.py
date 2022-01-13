net_type = 'resnet' #type=str,
workers = 4 # type=int, help='number of data loading workers (default: 4)'
epochs = 2 # type=int, metavar='N', help='number of total epochs to run'
batch_size = 128 #type=int, help='mini-batch size (default: 256)'
lr = 0.1 #help='initial learning rate')
momentum = 0.9 # help='momentum')
weight_decay = 1e-4 # type=float, help='weight decay (default: 1e-4)')
print_freq = 1  #help='print frequency (default: 10)')
depth = 32 # help='depth of the network (default: 32)')
dataset = "../../Datasets/Kvasir - Aziz" # help='Folder containing the dataset')
verbose = False # help='to print the status at every iteration')
alpha = 300 # type=float, help='number of new channel increases per depth (default: 300)')
expname = 'TEST' # help='name of experiment')
beta = 0 # type=float, help='hyperparameter beta')
cutmix_prob = 0 # type=float, help='cutmix probability')
iterations = 2 # type=int, help='Number of experiments to run')
