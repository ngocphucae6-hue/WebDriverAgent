import os, plistlib, subprocess
home = os.path.expanduser('~')
subprocess.run(['security', 'cms', '-D', '-i', home + '/Library/MobileDevice/Provisioning Profiles/profile.mobileprovision', '-o', '/tmp/profile.plist'], check=True)
with open('/tmp/profile.plist', 'rb') as f:
    profile = plistlib.load(f)
ent = profile['Entitlements']
team = profile.get('TeamIdentifier', [''])[0]
ent['application-identifier'] = team + '.' + os.environ['CI_BUNDLE_ID']
with open('/tmp/entitlements.plist', 'wb') as f:
    plistlib.dump(ent, f)
print('OK entitlements:', list(ent.keys()))