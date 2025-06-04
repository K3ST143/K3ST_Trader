import os

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure():
    # Directories
    directories = [
        'K3STTrader/backend/app',
        'K3STTrader/frontend/public',
        'K3STTrader/frontend/src/components',
        'K3STTrader/frontend/src/pages',
        'K3STTrader/database/migrations',
        'K3STTrader/database/models',
        'K3STTrader/database/seeds',
        'K3STTrader/docs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Files with their initial content
    files = {
        'K3STTrader/backend/app/__init__.py': '',
        'K3STTrader/backend/app/models.py': '',
        'K3STTrader/backend/app/routes.py': '',
        'K3STTrader/backend/app/utils.py': '',
        'K3STTrader/backend/app/education_routes.py': '',
        'K3STTrader/backend/app/receptionist_routes.py': '',
        'K3STTrader/backend/app/ai_receptionist.py': '',
        'K3STTrader/backend/app/stock_routes.py': '',
        'K3STTrader/backend/app/investor_routes.py': '',
        'K3STTrader/backend/app/financial_routes.py': '',
        'K3STTrader/backend/app/corporate_routes.py': '',
        'K3STTrader/backend/app/compliance_routes.py': '',
        'K3STTrader/backend/config.py': '',
        'K3STTrader/backend/requirements.txt': '',
        'K3STTrader/backend/run.py': '',
        'K3STTrader/frontend/src/pages/HomePage.js': '',
        'K3STTrader/frontend/src/pages/LoginPage.js': '',
        'K3STTrader/frontend/src/pages/AdminDashboard.js': '',
        'K3STTrader/frontend/src/pages/VirtualCampus.js': '',
        'K3STTrader/frontend/src/pages/VirtualReceptionist.js': '',
        'K3STTrader/frontend/src/pages/StockDashboard.js': '',
        'K3STTrader/frontend/src/pages/InvestorDashboard.js': '',
        'K3STTrader/frontend/src/pages/FinancialDashboard.js': '',
        'K3STTrader/frontend/src/pages/CorporateDashboard.js': '',
        'K3STTrader/frontend/src/pages/ComplianceDashboard.js': '',
        'K3STTrader/frontend/src/App.js': '',
        'K3STTrader/frontend/src/index.js': '',
        'K3STTrader/frontend/src/i18n.js': '',
        'K3STTraderTrader/frontend/package.json': '',
        'K3STTrader/database/database.py': '',
        'K3STTrader/docs/README.md': '',
        'K3STTrader/docs/setup_guide.md': '',
        'K3STTrader/docs/user_guide.md': '',
        'K3STTrader/docs/Business_Conduct_and_Code_of_Ethics.pdf': '',
        'K3STTrader/docs/Corporate_Governance.pdf': '',
        'K3STTrader/docs/Innovation_Documentation.pdf': '',
        'K3STTrader/docs/Business_Plan.pdf': '',
        'K3STTrader/docs/Compliance_Reporting.pdf': '',
        'K3STTrader/.gitignore': ''
    }

    for path, content in files.items():
        create_file(path, content)

if __name__ == "__main__":
    create_project_structure()
