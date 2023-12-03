#!/usr/bin/env ruby

if ARGV[0]
	r = ARGV[0].scan(/[A-Z]/).join
	puts "#{r}"
end
