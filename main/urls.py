from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.db import connection
from django.http import HttpResponse

def test_database(request):
    try:
        with connection.cursor() as cursor:
            # Simple test query
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            
            # Test if we can create a table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test_table (
                    id SERIAL PRIMARY KEY,
                    test_text VARCHAR(255),
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            
            # Insert test data
            cursor.execute("INSERT INTO test_table (test_text) VALUES ('Database working!');")
            
            # Read it back
            cursor.execute("SELECT * FROM test_table ORDER BY created_at DESC LIMIT 5;")
            rows = cursor.fetchall()
            
        result = f"""
        <html>
        <body style="font-family: Arial; padding: 20px;">
            <h2>✅ Database Connection Test</h2>
            <p><strong>PostgreSQL Version:</strong> {version[0]}</p>
            <p><strong>Connection:</strong> SUCCESS ✓</p>
            <h3>Test Data:</h3>
            <table border="1" cellpadding="10">
                <tr><th>ID</th><th>Text</th><th>Created At</th></tr>
        """
        
        for row in rows:
            result += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
        
        result += """
            </table>
            <p><a href="/admin/">Go to Admin</a> | <a href="/">Home</a></p>
        </body>
        </html>
        """
        
        return HttpResponse(result)
        
    except Exception as e:
        return HttpResponse(f"""
        <html>
        <body style="color: red; font-family: Arial; padding: 20px;">
            <h2>❌ Database Connection Failed</h2>
            <p><strong>Error:</strong> {str(e)}</p>
            <p>Check your DATABASE_URL in Render environment variables.</p>
        </body>
        </html>
        """)



urlpatterns = [
    # Django Admin
    path("test-db/", test_database), 
    path("admin/", admin.site.urls),
    
    # Your App API
    path("api/", include("core.urls")),
    
    # Frontend Pages
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    
    path("login/", TemplateView.as_view(template_name="login.html"), name="login"),
    path("register/", TemplateView.as_view(template_name="register.html"), name="register"),
    path("store/", TemplateView.as_view(template_name="store.html"), name="store"),
]

# ✅ NO AUTO-CREATION IN URLS.PY - Security risk!
