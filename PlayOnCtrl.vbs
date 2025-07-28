Set fso = CreateObject("Scripting.FileSystemObject")
Set sh = CreateObject("WScript.Shell")
set a = wscript.arguments

x = ""
if a.count = 0 then
	Set h = CreateObject("htmlfile")
	x = H.ParentWindow.ClipboardData.GetData("text")
elseif a.count = 1 then
	x = a(0)
else
	x = WScript.ScriptFullName & ".m3u"
	set f1 = fso.createtextfile(x)
	for each fn in a
		f1.writeline fn
	next
	f1.close
end if

wscript.sleep 1000

tv = "[TV] Samsung 5 Series (40)"
WorkDir = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\"))
sh.CurrentDirectory  = WorkDir
cmd = "python.exe PlayOn.py c -n """ & tv & """ -o """ & x & """"
'msgbox cmd
sh.run cmd, 2