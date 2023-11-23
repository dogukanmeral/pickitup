import os
import calendar
import time

def file_mod_time(file_path):
	return time.localtime(os.path.getmtime(file_path))

def file_mod_month_year(mod_time):
	return calendar.month_abbr[mod_time.tm_mon], str(mod_time.tm_year)

def by_date(files, current_path):
	files_by_mod_dates = {}

	for file in files:
		files_by_mod_dates[file] = " ".join(file_mod_month_year(file_mod_time(f"{current_path}\{file}")))

	return files_by_mod_dates
