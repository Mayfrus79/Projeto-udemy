import subprocess

car_script = '''
set /p car=Enter car name: 
echo Car %car% registered successfully!
echo Warning: This is a demo warning 1>&2
'''

result = subprocess.run(
    car_script,
    input='Mustang\n',
    capture_output=True,
    text=True,
    shell=True  # Removido executable
)

print("✅ STDOUT (Output):")
print(result.stdout)

print("⚠️ STDERR (Errors):")
print(result.stderr)

print("📦 EXIT CODE:")
print(result.returncode)
