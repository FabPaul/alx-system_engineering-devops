#!/usr/bin/env ruby
# Ruby script that matches a given pattern
puts ARGV[0].scan(/\[from:(.*?)\]\s+\[to:(.*?)\]\s+\[flags:(.*?)\]/).join(',')
