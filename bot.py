# coding: utf-8 
# Import the game simulator
import interface as bbox 

# This is the main function - it is the agent's brain. Funciton takes environment state
# vector and returns an action that agent is to perform. it is enough to only modify  
# this function to create a proper agent. 

def get_action_by_state(state, verbose=0): 
    
    # If verbose = True enable detailed logging to console 
    if verbose: 
        # Print environment state vector 
        for i in range (n_features): 
            print("state[%d] = %f" % (i, state[i]))
            
        # Print current score and time (number of current game step)
        print("score = {}, time={}".format(bbox.get_score(), bbox.get_time()))
        
    # This simple bot always performs action number 0. Not so smart :) 
    action_to_do = 0 
    return action_to_do
    
    
# Participants do not have to modify the code below, but it could be useful to 
# understand what this code does 
n_features = n_actions = max_time = -1 

def prepare_box(): 
    global n_features, n_actions, max_time 
    
    # Reset the environment to the initial state, just in case 
    if bbox.is_level_loaded(): 
        bbox.reset_level()
    else: 
        # Load the game level 
        bbox.load_level('../levels/train_level.data', verbose=1)
        n_features = bbox.get_num_of_features()
        n_actions = bbox.get_num_of_actions()
        max_time = bbox.get_max_time()
    
    
def run_bbox(verbose=False):
    has_next =  1
    
    # Prepare environment - Load the game level
    prepare_box()
        
    while has_next: 
        # Get current environment state 
        state = bbox.get_state()
        
        # Choose an action to perform at current step 
        action = get_action_by_state(state)
        
        # Perform chosen action 
        # Function do_action(action) returns False if level is finished, 
        # Otherwise returns True 
        has_next = bbox.do_action(action) 
        
    # Finish the game simulation, print earned reward 
    # While submitting solutions make sure you do call finish()
    bbox.finish(verbose=1)
    
    
# Begin execution of the main program 
if __name__ == "__main__": 
    run_bbox(verbose=0)
        