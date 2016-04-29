# coding: utf-8 
# Import the game simulator
import interface as bbox 
import numpy as np 

# This is the main function - it is the agent's brain. Funciton takes environment state
# vector and returns an action that agent is to perform. it is enough to only modify  
# this function to create a proper agent. 

def get_action_by_state(state, verbose=0): 
    best_act = -1 
    best_val = -1e9
    
    for act in range(n_actions): 
        val = calc_reg_for_action(act, state)
        
        if val > best_val:
            best_val = val 
            best_act = act
    
    return best_act
    
    
n_features = 36
n_actions = 4 
max_time = -1 

def prepare_box(): 
    global n_features, n_actions, max_time 
    
    # Reset the environment to the initial state, just in case 
    if bbox.is_level_loaded(): 
        bbox.reset_level()
    else: 
        # Load the game level 
        bbox.load_level('levels/train_level.data', verbose=1)
        n_features = bbox.get_num_of_features()
        n_actions = bbox.get_num_of_actions()
        max_time = bbox.get_max_time()
    
    
def load_regression_coefs(file_name): 
    global reg_coefs, free_coefs
    coefs = np.loadtxt(file_name).reshape(n_actions, n_features +1)
    reg_coefs = coefs[:,:-1]
    free_coefs = coefs[:,-1]
    
def calc_reg_for_action(action, state): 
    return np.dot(reg_coefs[action], state) + free_coefs[action]    
    
def run_bbox(verbose=False):
    has_next =  1
    
    # Prepare environment - Load the game level
    prepare_box()

    # Load the regressions
    load_regression_coefs("regression_bot/reg_coefs.txt")
        
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
        