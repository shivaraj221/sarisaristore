#!/usr/bin/env bash
set -o errexit

echo "🚀 Starting Render build..."

# Install dependencies
pip install -r requirements.txt

# Debug: Show environment
echo "🔍 Environment check:"
echo "DATABASE_URL: ${DATABASE_URL:0:50}..."  # Show first 50 chars
echo "DEBUG: $DEBUG"

# Apply migrations
echo "📦 Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Build completed!"
