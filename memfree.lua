#!/usr/bin/env luajit

--[[
        This lua script acts similar to the 'free' command, which will
        display some interesting information about how much memory is being
        used in the system.

        This example assumes lj2procfs is installed into the lua path
--]]


local procfs = require("lj2procfs.procfs")

local meminfo = procfs.meminfo;

local memtotal = meminfo.MemTotal.size
local memfree = meminfo.MemFree.size
local memused = memtotal - memfree
local memshared = meminfo.Shmem.size
local membuffers = meminfo.Buffers.size
local memcached = meminfo.Cached.size

local swaptotal = meminfo.SwapTotal.size

print(string.format("%s", memtotal))
print(string.format("%s", memused))
print(string.format("%s", memfree))
print(string.format("%s", membuffers))
print(string.format("%s", memcached))

--print(string.format(memtotal, memused, memfree, memshared, membuffers, memcached))
--print(string.format("-/+ buffers/cache: %10d %10d", 1, 2))
--print(string.format("Swap: %12d %10d %10d", swaptotal, swapused, swapfree))