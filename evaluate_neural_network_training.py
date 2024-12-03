"""  
Neural Network Training Expert System  

This application provides an interactive GUI for evaluating neural network   
training parameters using an expert system built with CLIPS.  

Dependencies:  
- tkinter for GUI  
- clips for expert system logic  
"""  

import tkinter as tk  
from tkinter import ttk  
import clips  

def evaluate_model():  
    """  
    Evaluate the neural network model using CLIPS expert system.  
    
    Collects parameter values from GUI sliders, asserts facts in CLIPS,  
    runs the expert system, and displays advice.  
    """  
    env = clips.Environment()  

    # Load CLIPS rules for evaluation  
    env.load('evaluate_neural_network_training_1.CLP')  
    
    # Collect input parameters from GUI sliders  
    input_params = {  
        'accuracy': float(accuracy_slider.get()),  
        'loss': float(loss_slider.get()),  
        # ... (add other parameters)  
    }  

    # Assert performance facts to CLIPS environment  
    env.assert_string(f'(performance ...)')  # Your existing assertion logic  

    # Run expert system rules  
    env.run()  

    # Collect and display advice  
    advice_list = [str(fact) for fact in env.facts() if fact.template.name == 'advice']  
    advice_text.delete(1.0, tk.END)  
    advice_text.insert(tk.END, '\n'.join(advice_list))  

def create_slider(label, row, from_, to, resolution, default):  
    """  
    Create a labeled slider for parameter input.  
    
    Args:  
        label (str): Label for the slider  
        row (int): Grid row position  
        from_ (float): Minimum slider value  
        to (float): Maximum slider value  
        resolution (float): Slider step value  
        default (float): Default slider position  
    
    Returns:  
        tk.Scale: Created slider widget  
    """  
    tk.Label(root, text=label).grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)  
    slider = tk.Scale(root, from_=from_, to=to, orient=tk.HORIZONTAL, resolution=resolution)  
    slider.set(default)  
    slider.grid(row=row, column=1, padx=10, pady=5)  
    return slider  

# Create the main window
root = tk.Tk()
root.title("Neural Network Evaluator")
root.geometry("600x700")

accuracy_slider = create_slider("Accuracy:", 0, 0.0, 1.0, 0.01, 0.5)
loss_slider = create_slider("Loss:", 1, 0.0, 1.0, 0.01, 0.5)
epochs_slider = create_slider("Epochs:", 2, 1, 100, 1, 10)
train_accuracy_slider = create_slider("Training Accuracy:", 3, 0.0, 1.0, 0.01, 0.5)
val_accuracy_slider = create_slider("Validation Accuracy:", 4, 0.0, 1.0, 0.01, 0.5)
learning_rate_slider = create_slider("Learning Rate:", 5, 0.0001, 0.1, 0.0001, 0.001)
batch_size_slider = create_slider("Batch Size:", 6, 16, 512, 16, 32)
model_complexity_slider = create_slider("Model Complexity (Layers):", 7, 1, 30, 1, 5)

# Create button to evaluate the model
evaluate_button = ttk.Button(root, text="Evaluate Model", command=evaluate_model)
evaluate_button.grid(row=8, column=0, columnspan=2, pady=20)

# Create text box to display advice
tk.Label(root, text="Advice:").grid(row=9, column=0, sticky=tk.W, padx=10, pady=5)
advice_text = tk.Text(root, height=10, width=70)
advice_text.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
