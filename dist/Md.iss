; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "PaymentBook"
#define MyAppVersion "1.0"
#define MyAppPublisher "Md Arshad Ali"
#define MyAppExeName "mess.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{0777D011-0FF9-40B1-9649-3A66D1B21408}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; The [Icons] "quicklaunchicon" entry uses {userappdata} but its [Tasks] entry has a proper IsAdminInstallMode Check.
UsedUserAreasWarning=no
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\Md Arshad Ali\Desktop\panjab mess
OutputBaseFilename=mysetup
SetupIconFile=C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\favicon (7).ico
Password=0089
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\mess.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\__pycache__\*"; DestDir: "{app}\__pycache__"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\build\mess\*"; DestDir: "{app}\mess"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\bills\*"; DestDir: "{app}\bills"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\list\*"; DestDir: "{app}\list"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\favicon (7).ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\icons8-book-64.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Md Arshad Ali\Desktop\panjab mess\dist\icons8-khanda-96.png"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
