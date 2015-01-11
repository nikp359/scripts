#!/bin/bash
TMUX_CONFIG="/home/nik/.tmux.conf"
echo "Tmux init"
if [ -f "$TMUX_CONFIG" ]; then
	echo "set -g terminal-overrides 'xterm*:smcup@:rmcup@'" >> $TMUX_CONFIG
else
	pwd ~
	#touch $TMUX_CONFIG
	echo "set -g terminal-overrides 'xterm*:smcup@:rmcup@'" >> $TMUX_CONFIG
fi
