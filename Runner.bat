@echo off
%~d0
cd %~dp0
cmd "/c activate cdap && python -m GUI.FundamentalIssueGUI && deactivate"