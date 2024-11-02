import os

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure():
    # Directories
    directories = [
        'AddisGlobalTrader/backend/app',
        'AddisGlobalTrader/frontend/public',
        'AddisGlobalTrader/frontend/src/components',
        'AddisGlobalTrader/frontend/src/pages',
        'AddisGlobalTrader/database/migrations',
        'AddisGlobalTrader/database/models',
        'AddisGlobalTrader/database/seeds',
        'AddisGlobalTrader/docs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Files with their initial content
    files = {
        'AddisGlobalTrader/backend/app/__init__.py': '',
        'AddisGlobalTrader/backend/app/models.py': '',
        'AddisGlobalTrader/backend/app/routes.py': '',
        'AddisGlobalTrader/backend/app/utils.py': '',
        'AddisGlobalTrader/backend/app/education_routes.py': '',
        'AddisGlobalTrader/backend/app/receptionist_routes.py': '',
        'AddisGlobalTrader/backend/app/ai_receptionist.py': '',
        'AddisGlobalTrader/backend/app/stock_routes.py': '',
        'AddisGlobalTrader/backend/app/investor_routes.py': '',
        'AddisGlobalTrader/backend/app/financial_routes.py': '',
        'AddisGlobalTrader/backend/app/corporate_routes.py': '',
        'AddisGlobalTrader/backend/app/compliance_routes.py': '',
        'AddisGlobalTrader/backend/config.py': '',
        'AddisGlobalTrader/backend/requirements.txt': '',
        'AddisGlobalTrader/backend/run.py': '',
        'AddisGlobalTrader/frontend/src/pages/HomePage.js': '',
        'AddisGlobalTrader/frontend/src/pages/LoginPage.js': '',
        'AddisGlobalTrader/frontend/src/pages/AdminDashboard.js': '',
        'AddisGlobalTrader/frontend/src/pages/VirtualCampus.js': '',
        'AddisGlobalTrader/frontend/src/pages/VirtualReceptionist.js': '',
        'AddisGlobalTrader/frontend/src/pages/StockDashboard.js': '',
        'AddisGlobalTrader/frontend/src/pages/InvestorDashboard.js': '',
        'AddisGlobalTrader/frontend/src/pages/FinancialDashboard.js': '',
        'AddisGlobalTrader/frontend/src/pages/CorporateDashboard.js': '',
        'AddisGlobalTrader/frontend/src/pages/ComplianceDashboard.js': '',
        'AddisGlobalTrader/frontend/src/App.js': '',
        'AddisGlobalTrader/frontend/src/index.js': '',
        'AddisGlobalTrader/frontend/src/i18n.js': '',
        'AddisGlobalTrader/frontend/package.json': '',
        'AddisGlobalTrader/database/database.py': '',
        'AddisGlobalTrader/docs/README.md': '',
        'AddisGlobalTrader/docs/setup_guide.md': '',
        'AddisGlobalTrader/docs/user_guide.md': '',
        'AddisGlobalTrader/docs/Business_Conduct_and_Code_of_Ethics.pdf': '',
        'AddisGlobalTrader/docs/Corporate_Governance.pdf': '',
        'AddisGlobalTrader/docs/Innovation_Documentation.pdf': '',
        'AddisGlobalTrader/docs/Business_Plan.pdf': '',
        'AddisGlobalTrader/docs/Compliance_Reporting.pdf': '',
        'AddisGlobalTrader/.gitignore': ''
    }

    for path, content in files.items():
        create_file(path, content)

if __name__ == "__main__":
    create_project_structure()
