# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZYEApd6QA5ZwNLcibTlf0Db3xqLQlGt
"""



"""TESTING THE MODEL"""

def predict_gender(name):
    model.eval()
    with torch.no_grad():
        name_tensor = name_to_tensor(name).unsqueeze(0).to(device)
        hidden = model.init_hidden()
        output, hidden = model(name_tensor, hidden)
        gender_pred = torch.argmax(output).item()
        return 'Female' if gender_pred == 0 else 'Male'

test_names = ['Emma', 'John', 'Sophia', 'George', 'Olivia']
for name in test_names:
    gender = predict_gender(name)
    print(f'Name: {name}, Predicted Gender: {gender}')

predict_gender("Eyimode")