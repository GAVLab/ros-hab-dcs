tmux new-session \; \
	send-keys 'roslaunch full_flight.launch' C-m \; \
	split-window -h \; \
	send-keys 'python3 display_full.py' C-m \; \
	split-window -v \; \
	select-pane -t 0 \; \
	split-window -v \; \
	send-keys './record_full.sh' C-m \; \
