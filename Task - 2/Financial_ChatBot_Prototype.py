import pandas as pd

# Reading the Excel files
try:
    final_report = pd.read_excel('T:/1. PROJECTS/BCG X - GEN AI/Task - 1/final_data_report.xlsx')
    summary_report = pd.read_excel('T:/1. PROJECTS/BCG X - GEN AI/Task - 1/report_summary.xlsx')
except Exception as e:
    print(f"Error reading files: {e}")

# Extract year from 'Fiscal Year End' and create a 'Year' column in final_report
final_report['Year'] = final_report['Fiscal Year End'].str.extract(r'(\d{4})').astype(float)

def financial_chatbot():
    print("\nPlease enter your query")
    user_query = input().strip()

    # Check if data for the selected year is available
    if fiscal_year not in available_years:
        return f"Data for fiscal year {fiscal_year} is not available for {company_input}."

    if user_query == "What is the total revenue?":
        revenue = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Revenue'].values[0]
        return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
    
    elif user_query == "What is the Net Income?":
        net_income = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income'].values[0]
        return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
    
    elif user_query == "What is the sum of total assets?":
        total_assets = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Assets'].values[0]
        return f"The sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets}"
    
    elif user_query == "What is the sum of total liabilities?":
        total_liabilities = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Liabilities'].values[0]
        return f"The sum of Total Liabilities for {company_input} for fiscal year {fiscal_year} is $ {total_liabilities}"
    
    elif user_query == "What is cash flow from operating activities?":
        cash_ops = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
        return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops}"
    
    elif user_query == "What is the revenue growth(%) ?":
        revenue_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
    
    elif user_query == "What is the net income growth(%) ?":
        net_income_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_income_growth}(%)"
    
    elif user_query == "What is the assets growth(%) ?":
        assets_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {assets_growth}(%)"
    
    elif user_query == "What is the liabilities growth(%) ?":
        liabilities_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
        return f"The Liabilities Growth(%) for {company_input} for fiscal year {fiscal_year} is {liabilities_growth}(%)"
    
    elif user_query == "What is the cash flow from operations growth(%) ?":
        cash_ops_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {cash_ops_growth}(%)"
    
    elif user_query == "What is the year by year average revenue growth rate(%)?":
        year_avg_revenue_growth = summary_report[(summary_report['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Revenue Growth Rate(%) For Last 3 Fiscal Year End for {company_input} is {year_avg_revenue_growth}(%)"
     
    elif user_query == "What is the year by year average net income growth rate(%)?":
        year_avg_net_income_growth = summary_report[(summary_report['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Year By Year Net Income Revenue Growth Rate(%) For Last 3 Fiscal Year End for {company_input} is {year_avg_net_income_growth}(%)"
    
    elif user_query == "What is the year by year average assets growth rate(%)?":
        year_avg_assets_growth = summary_report[(summary_report['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Assets Growth Rate(%) For Last 3 Fiscal Year End for {company_input} is {year_avg_assets_growth}(%)"
    
    elif user_query == "What is the year by year average liabilities growth rate(%)?":
        year_avg_liabilities_growth = summary_report[(summary_report['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Liabilities Growth Rate(%) For Last 3 Fiscal Year End for {company_input} is {year_avg_liabilities_growth}(%)"
    
    elif user_query == "What is the year by year average cash flow from operations growth rate(%)?":
        year_avg_cash_ops_growth = summary_report[(summary_report['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) For Last 3 Fiscal Year End for {company_input} is {year_avg_cash_ops_growth}(%)" 
    
    else:
        return "Sorry, I cannot only provide information on the requested query."

# Test the chatbot
while True:
    print("----------------------------------------------------------------------------")
    user_input = input("\nEnter Hi to start the chatbot session; type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "hi":
        print("\nHello! Welcome to AI Driven Financial Chatbot!!!")
        print("\nI can help you with your financial queries")
        print("Please select the company name from below: -")
        print("\n1.Microsoft \n2.Tesla \n3.Apple")
        company_input = input("Enter company name : ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid Company Name. Please check and enter correct company name by starting the chatbot session again")
            break
        else:
            print('\nFor "Tesla" and "Apple", The data  is currently available for the fiscal year 2023, 2022, and 2021')
            print('\nAnd for "Microsoft" only, The data is currently available for the fiscal year 2024, 2023 and 2022')
            fiscal_year = int(input('\nThe fiscal year for the selected company :'))
            if (fiscal_year not in [2023, 2022, 2021] and company_input in ['Apple', 'Tesla']) or (fiscal_year not in [2024, 2023, 2022] and company_input in ['Microsoft']):
                print(f"\nYou entered company name : \"{company_input}\" and year : \"{fiscal_year}\", Please enter a valid fiscal year by starting the chatbot session again")
                break
            
            # Check available years for the selected company
            available_years = final_report[final_report['Company'] == company_input]['Year'].unique()

    else:
        print("Enter 'Hi' Properly!!!!! by starting the chatbot session again")
        break
            
    response = financial_chatbot()
    print(response)
