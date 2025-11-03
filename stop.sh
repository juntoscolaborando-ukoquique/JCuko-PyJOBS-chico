#!/bin/bash

# ==============================================================================
# Job Organizer (Reflex) - Stop Script
# ==============================================================================
# Stops all running Reflex processes
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
print_info "Stopping Job Organizer (Reflex)..."
echo ""

# Find and kill all reflex processes
REFLEX_PROCESSES=$(pgrep -f "reflex run" | tr '\n' ' ')

if [ -z "$REFLEX_PROCESSES" ]; then
    print_warning "No Reflex processes found running"
else
    print_info "Found Reflex processes: $REFLEX_PROCESSES"
    print_info "Stopping Reflex processes..."

    # Kill all reflex processes
    kill -9 $REFLEX_PROCESSES 2>/dev/null

    # Wait a moment
    sleep 2

    # Check if they were killed
    if pgrep -f "reflex run" > /dev/null; then
        print_error "Failed to stop all Reflex processes"
        print_error "Try manually: pkill -9 -f 'reflex run'"
        exit 1
    else
        print_success "Reflex processes stopped successfully"
    fi
fi

# Also kill any bun processes (frontend dev server)
BUN_PROCESSES=$(pgrep -f "bun.*run dev" | tr '\n' ' ')

if [ -n "$BUN_PROCESSES" ]; then
    print_info "Found Bun processes: $BUN_PROCESSES"
    print_info "Stopping Bun processes..."
    pkill -f "bun.*run dev"
    print_success "Bun processes stopped successfully"
fi

# Clean up any leftover processes
print_info "Cleaning up any remaining processes..."
pkill -f "reflex" 2>/dev/null
pkill -f "bun" 2>/dev/null

print_success "All processes stopped!"
echo ""
print_info "You can now safely run './start.sh' again if needed"
echo ""
