#!/usr/bin/env python3
"""
Verification Script - Check if application is ready to run
Run this: python verify.py
"""

import os
import sys
import subprocess

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

    def print_header():
        print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE} AI-Enhanced Onboarding - Verification{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

        def check_python():
            """Check Python version"""
            print(f"{Colors.BLUE} Checking Python...{Colors.END}")

            if sys.version_info < (3, 7):
                print(f"{Colors.RED} Python 3.7+ required{Colors.END}")
                print(f" Current: {sys.version}")
            return False

            print(f"{Colors.GREEN} Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}{Colors.END}")
        return True

        def check_flask():
            """Check if Flask is installed"""
            print(f"{Colors.BLUE} Checking Flask...{Colors.END}")

            try:
                import flask
                print(f"{Colors.GREEN} Flask {flask.__version__} installed{Colors.END}")
                return True
            except ImportError:
                print(f"{Colors.YELLOW} Flask not installed{Colors.END}")
                print(f" Run: pip install flask")
                return False

        def check_files():
            """Check if all required files exist"""
            print(f"{Colors.BLUE} Checking files...{Colors.END}")

            required_files = [
            'app.py',
            'OnBoard.py',
            'requirements.txt',
            'templates/index.html',
            'static/style.css',
            'static/script.js',
            'config.py',
            'README.md',
            'QUICKSTART.md'
            ]

            all_exist = True
            for file in required_files:
                path = os.path.join(os.getcwd(), file)
                if os.path.exists(path):
                    print(f"{Colors.GREEN} {file}{Colors.END}")
                else:
                    print(f"{Colors.RED} {file} (missing){Colors.END}")
                    all_exist = False

                return all_exist

                def check_content():
                    """Check if content files have substance"""
                    print(f"{Colors.BLUE} Checking content...{Colors.END}")

                    try:
                        with open('app.py', 'r') as f:
                            content = f.read()
                            if 'ONBOARDING_BOARD' in content and 'AI_INSIGHTS' in content:
                                print(f"{Colors.GREEN} Onboarding content found{Colors.END}")
                                return True
                            else:
                                print(f"{Colors.RED} Content incomplete{Colors.END}")
                            return False
                    except Exception as e:
                        print(f"{Colors.RED} Error reading content: {e}{Colors.END}")
                    return False

                    def main():
                        print_header()

                        checks = [
                        ("Python Version", check_python),
                        ("Flask Installation", check_flask),
                        ("Required Files", check_files),
                        ("Content Files", check_content),
                        ]

                        results = []
                        for name, check_func in checks:
                            try:
                                result = check_func()
                                results.append((name, result))
                            except Exception as e:
                                print(f"{Colors.RED} Error in {name}: {e}{Colors.END}")
                                results.append((name, False))
                                print()

                                # Summary
                                print(f"{Colors.BLUE}{'='*60}{Colors.END}")
                                print(f"{Colors.BLUE} Summary{Colors.END}")
                                print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

                                all_passed = True
                                for name, result in results:
                                    status = f"{Colors.GREEN} PASS{Colors.END}" if result else f"{Colors.RED} FAIL{Colors.END}"
                                    print(f"{status} {name}")
                                    if not result:
                                        all_passed = False

                                        print()

                                        if all_passed:
                                            print(f"{Colors.GREEN} All checks passed!{Colors.END}")
                                            print(f"\n{Colors.BLUE}To start the application:{Colors.END}")
                                            print(f" {Colors.YELLOW}python OnBoard.py{Colors.END}")
                                            print(f"\n{Colors.BLUE}Then open:{Colors.END}")
                                            print(f" {Colors.YELLOW}http://localhost:5000{Colors.END}\n")
                                        return 0
                                    else:
                                        print(f"{Colors.RED} Some checks failed. See above for details.{Colors.END}\n")

                                        # Try to install Flask if missing
                                        try:
                                            import flask
                                        except ImportError:
                                            print(f"{Colors.YELLOW}Installing Flask...{Colors.END}")
                                            subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "-q"])
                                            print(f"{Colors.GREEN}Flask installed!{Colors.END}")
                                            print(f"\n{Colors.BLUE}Run this again: python verify.py{Colors.END}\n")

                                        return 1

                                        if __name__ == '__main__':
                                            sys.exit(main())
