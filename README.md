My attempt at understanding and implementing the diamond-square algorithm, that allows for procedural map generation.

Latest version: 1.0, 02/12/2016

To be improved: vertices of each square being stored more than once. Array length / storage cost higher than expected.

## Haxe version
In order to run the Haxe version, you need [haxe][http://haxe.org] and [kha](http://kha.tech).

I recommend you install kha via `haxelib git`.
```
haxelib git kha https://github.com/KTXSoftware/Kha.git
```

Then, in my .bashrc (or .zshrc) I added an alias where `alias kha="node /$KHA_PATH/make $@"`, after setting the environment variable `$KHA_PATH`.

Alternatively, you can set up a script in the root of the project, pointing at your kha library.

Running `kha [target]` (e.g. `kha html5`) will create the project files for that target, in case of native targets (linux/windows/osx) you can additionally provide `--compile` to compile the project or `--run` to compile and run the project automatically. The target argument can be omitted if you wish to build for your current target (e.g. `kha` will build for linux when running on linux).

The example shows a 1024x1024 square with 5 iterations applied, the size of the single points is 20 plus the z value, with deviation of 10.

The plan is to move the algorithm to his own module so it can be reused without Kha.
