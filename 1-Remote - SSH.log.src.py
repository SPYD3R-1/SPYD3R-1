[16:54:17.070] Log Level: 2
[16:54:17.073] SSH Resolver called for "ssh-remote+7b22686f73744e616d65223a2248697376706e2e6f7267227d", attempt 1
[16:54:17.073] "remote.SSH.useLocalServer": true
[16:54:17.073] "remote.SSH.useExecServer": true
[16:54:17.073] "remote.SSH.path": undefined
[16:54:17.073] "remote.SSH.configFile": undefined
[16:54:17.073] "remote.SSH.useFlock": true
[16:54:17.073] "remote.SSH.lockfilesInTmp": false
[16:54:17.074] "remote.SSH.localServerDownload": auto
[16:54:17.074] "remote.SSH.remoteServerListenOnSocket": false
[16:54:17.074] "remote.SSH.showLoginTerminal": false
[16:54:17.074] "remote.SSH.defaultExtensions": []
[16:54:17.074] "remote.SSH.loglevel": 2
[16:54:17.074] "remote.SSH.enableDynamicForwarding": true
[16:54:17.074] "remote.SSH.enableRemoteCommand": false
[16:54:17.074] "remote.SSH.serverPickPortsFromRange": {}
[16:54:17.074] "remote.SSH.serverInstallPath": {}
[16:54:17.074] "remote.SSH.permitPtyAllocation": false
[16:54:17.074] "remote.SSH.preferredLocalPortRange: undefined
[16:54:17.074] "remote.SSH.useCurlAndWgetConfigurationFiles: false
[16:54:17.076] VS Code version: 1.92.0
[16:54:17.076] Remote-SSH version: remote-ssh@0.113.1
[16:54:17.076] darwin arm64
[16:54:17.076] SSH Resolver called for host: Hisvpn.org
[16:54:17.076] Setting up SSH remote "Hisvpn.org"
[16:54:17.078] Acquiring local install lock: /var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-remote-ssh-205b1191-install.lock
[16:54:17.078] Looking for existing server data file at /Users/ariseai.py/Library/Application Support/Code/User/globalStorage/ms-vscode-remote.remote-ssh/vscode-ssh-host-205b1191-b1c0a14de1414fcdaa400695b4db1c0799bc3124-0.113.1-es/data.json
[16:54:17.078] Using commit id "b1c0a14de1414fcdaa400695b4db1c0799bc3124" and quality "stable" for server
[16:54:17.080] Install and start server if needed
[16:54:17.081] PATH: /Library/Frameworks/Python.framework/Versions/3.12/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
[16:54:17.081] Checking ssh with "ssh -V"
[16:54:17.085] > OpenSSH_9.7p1, LibreSSL 3.3.6

[16:54:17.086] askpass server listening on /var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-ssh-askpass-b2ea16c14af762a32ff35e4819fcc523fa136282.sock
[16:54:17.087] Spawning local server with {"serverId":1,"ipcHandlePath":"/var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-ssh-askpass-f17067f7e2af9cf5023f1824898c7d29629350e0.sock","sshCommand":"ssh","sshArgs":["-v","-T","-D","50260","-o","ConnectTimeout=15","Hisvpn.org"],"serverDataFolderName":".vscode-server","dataFilePath":"/Users/ariseai.py/Library/Application Support/Code/User/globalStorage/ms-vscode-remote.remote-ssh/vscode-ssh-host-205b1191-b1c0a14de1414fcdaa400695b4db1c0799bc3124-0.113.1-es/data.json"}
[16:54:17.087] Local server env: {"SSH_AUTH_SOCK":"/private/tmp/com.apple.launchd.s7Q45ag81z/Listeners","SHELL":"/bin/zsh","DISPLAY":"1","ELECTRON_RUN_AS_NODE":"1","SSH_ASKPASS":"/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/local-server/askpass.sh","VSCODE_SSH_ASKPASS_NODE":"/private/var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/AppTranslocation/3D06009F-27E4-4390-A394-B4C88AF65DD8/d/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin)","VSCODE_SSH_ASKPASS_EXTRA_ARGS":"","VSCODE_SSH_ASKPASS_MAIN":"/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/askpass-main.js","VSCODE_SSH_ASKPASS_HANDLE":"/var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-ssh-askpass-b2ea16c14af762a32ff35e4819fcc523fa136282.sock"}
[16:54:17.087] Spawned 25189
[16:54:17.140] > local-server-1> Running ssh connection command: ssh -v -T -D 50260 -o ConnectTimeout=15 Hisvpn.org
[16:54:17.141] > local-server-1> Spawned ssh, pid=25193
[16:54:17.143] stderr> OpenSSH_9.7p1, LibreSSL 3.3.6
[16:54:17.145] stderr> ssh: Could not resolve hostname axtlabs: nodename nor servname provided, or not known
[16:54:17.146] > local-server-1> ssh child died, shutting down
[16:54:17.148] Local server exit: 0
[16:54:17.148] Received install output: local-server-1> Running ssh connection command: ssh -v -T -D 50260 -o ConnectTimeout=15 Hisvpn.org
local-server-1> Spawned ssh, pid=25193
OpenSSH_9.7p1, LibreSSL 3.3.6
ssh: Could not resolve hostname axtlabs: nodename nor servname provided, or not known
local-server-1> ssh child died, shutting down

[16:54:17.150] Resolver error: Error: Could not resolve hostname
	at m.Offline (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:501281)
	at /Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:496940
	at t.handleInstallOutput (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:497487)
	at e (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:560378)
	at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
	at async /Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:582435
	at async t.withShowDetailsEvent (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:586054)
	at async /Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:557083
	at async T (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:555134)
	at async t.resolveWithLocalServer (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:556623)
	at async k (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:579574)
	at async t.resolve (/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:583465)
	at async /Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/extension.js:2:851126
[16:54:17.152] ------




[16:54:17.219] Opening exec server for ssh-remote+7b22686f73744e616d65223a2248697376706e2e6f7267227d
[16:54:17.224] Acquiring local install lock: /var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-remote-ssh-205b1191-install.lock
[16:54:17.224] Initizing new exec server for ssh-remote+7b22686f73744e616d65223a2248697376706e2e6f7267227d
[16:54:17.235] Looking for existing server data file at /Users/ariseai.py/Library/Application Support/Code/User/globalStorage/ms-vscode-remote.remote-ssh/vscode-ssh-host-205b1191-b1c0a14de1414fcdaa400695b4db1c0799bc3124-0.113.1-es/data.json
[16:54:17.235] Using commit id "b1c0a14de1414fcdaa400695b4db1c0799bc3124" and quality "stable" for server
[16:54:17.236] Install and start server if needed
[16:54:17.237] askpass server listening on /var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-ssh-askpass-01dc90b519632932d3f21d1f66527e799f998cb9.sock
[16:54:17.237] Spawning local server with {"serverId":2,"ipcHandlePath":"/var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-ssh-askpass-acd22b82b07eedcbce5e932adbc2e3b512a6f4c7.sock","sshCommand":"ssh","sshArgs":["-v","-T","-D","50260","-o","ConnectTimeout=15","Hisvpn.org"],"serverDataFolderName":".vscode-server","dataFilePath":"/Users/ariseai.py/Library/Application Support/Code/User/globalStorage/ms-vscode-remote.remote-ssh/vscode-ssh-host-205b1191-b1c0a14de1414fcdaa400695b4db1c0799bc3124-0.113.1-es/data.json"}
[16:54:17.237] Local server env: {"SSH_AUTH_SOCK":"/private/tmp/com.apple.launchd.s7Q45ag81z/Listeners","SHELL":"/bin/zsh","DISPLAY":"1","ELECTRON_RUN_AS_NODE":"1","SSH_ASKPASS":"/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/local-server/askpass.sh","VSCODE_SSH_ASKPASS_NODE":"/private/var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/AppTranslocation/3D06009F-27E4-4390-A394-B4C88AF65DD8/d/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin)","VSCODE_SSH_ASKPASS_EXTRA_ARGS":"","VSCODE_SSH_ASKPASS_MAIN":"/Users/ariseai.py/.vscode/extensions/ms-vscode-remote.remote-ssh-0.113.1/out/askpass-main.js","VSCODE_SSH_ASKPASS_HANDLE":"/var/folders/vb/6qzcpyq57ml8v7r3rzml56s00000gn/T/vscode-ssh-askpass-01dc90b519632932d3f21d1f66527e799f998cb9.sock"}
[16:54:17.237] Spawned 25194
[16:54:17.290] > local-server-2> Running ssh connection command: ssh -v -T -D 50260 -o ConnectTimeout=15 Hisvpn.org
[16:54:17.291] > local-server-2> Spawned ssh, pid=25198
[16:54:17.294] stderr> OpenSSH_9.7p1, LibreSSL 3.3.6
[16:54:17.296] stderr> ssh: Could not resolve hostname axtlabs: nodename nor servname provided, or not known
[16:54:17.297] > local-server-2> ssh child died, shutting down
[16:54:17.299] Local server exit: 0
[16:54:17.299] Received install output: local-server-2> Running ssh connection command: ssh -v -T -D 50260 -o ConnectTimeout=15 Hisvpn.org
local-server-2> Spawned ssh, pid=25198
OpenSSH_9.7p1, LibreSSL 3.3.6
ssh: Could not resolve hostname axtlabs: nodename nor servname provided, or not known
local-server-2> ssh child died, shutting down

[16:54:17.299] Exec server for ssh-remote+7b22686f73744e616d65223a2248697376706e2e6f7267227d failed: Error: Could not resolve hostname
[16:54:17.299] Error opening exec server for ssh-remote+7b22686f73744e616d65223a2248697376706e2e6f7267227d: Error: Could not resolve hostname

	<\html>
		<\aguments forwarded from useLocalServer to enableRemoteCommand>
			pixels, frames pre second, specifications : axt server , axt database , axtTerminal key , 