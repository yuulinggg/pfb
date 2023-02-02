#Importing the other files containing the functions we need to run the main function.
import cash_on_hand, overheads, profit_loss
#Defining the main function and setting no parameters.
def main():
    """
    This function will run the other functions to generate the data required.
    """
#Binding the profit loss value to the profit loss function.
    profit_loss_value = profit_loss.profit_loss_function()
#Binding the overhead value to the overhead function.
    overhead_value = overheads.overhead_function()
#Binding the cash on hand value to the cash on hand function.
    cash_on_hand_value = cash_on_hand.cash_on_hand_function()
    
#Creating a text file named "summary_report.txt" to store our summary report.
    with open('summary_report.txt', 'w') as file:
#Writing the summary report with the values generated.
        file.write(f"{overhead_value}{cash_on_hand_value}{profit_loss_value}")
#Calling the main function.
main()
#Setting file path.
from pathlib import Path
#Setting a variable for team members names with file path and naming it "team_members.txt".
team_path = Path.cwd()/ "team_members.txt"
#Creating the text file.
team_path.touch()
#Writing team members names with student number in the text file.
with team_path.open(mode = "w", encoding="UTF-8") as file:
    file.write("Cai Cheng Wei S10220897F\nJanice Chong Xiao Lin S10242714F\nLim Shi Qi S10221151B\nLow Yu Ling S10220905B\nZack Arthur Cloney S10243549G")
