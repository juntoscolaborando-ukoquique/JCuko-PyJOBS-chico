#!/bin/bash

# ==============================================================================
# Job Organizer (Reflex) - Minimal Version Startup Script
# ==============================================================================

# Colors
C_RESET='\033[0m'
C_GREEN='\033[0;32m'
C_BLUE='\033[0;34m'
C_YELLOW='\033[0;33m'
C_RED='\033[0;31m'

print_info() {
    echo -e "${C_BLUE}[INFO]${C_RESET} $1"
}

print_success() {
    echo -e "${C_GREEN}[SUCCESS]${C_RESET} $1"
}

print_warning() {
    echo -e "${C_YELLOW}[WARNING]${C_RESET} $1"
}

print_error() {
    echo -e "${C_RED}[ERROR]${C_RESET} $1"
}

echo ""
print_info "Starting Job Organizer (Minimal Version)..."
echo ""

# Check if reflex is installed
if ! command -v reflex &> /dev/null; then
    print_error "Reflex is not installed."
    echo "Please install it with: pip install -r requirements.txt"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "rxconfig.py" ]; then
    print_error "rxconfig.py not found."
    echo "Please run this script from the project root directory."
    exit 1
fi

# Initialize Reflex if needed (first time setup)
if [ ! -d ".web" ]; then
    print_info "First time setup - initializing Reflex..."
    reflex init
fi

# Start the Reflex app
print_info "Starting Reflex application..."
echo ""
print_success "Reflex is starting up..."
echo ""
echo "  📱 Frontend: http://localhost:3000"
echo "  🔧 Backend: http://localhost:8000"
echo ""
echo "  Press Ctrl+C to stop the server"
echo ""

reflex run
