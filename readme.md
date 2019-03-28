# Developer portal
Front end for showing the api catalog, data sources and other development resources.

![Logo example](https://raw.githubusercontent.com/eirikbroen/cuem/master/micro.png)

<p>
      <a href="#how-to-install-and-run">Installation</a><br>
      <a href="#how-to-test">Test</a><br>
      <a href="#quickstart">Quickstart</a><br>
      <a href="#environment">Environment</a>
      <a href="#project-setup">Setup</a>
    </p>

## How to install and run
Make sure you have node 11.8.0. Tip: Install nvm.
```
# Install
make init

# Run
make run
```

## How to test
```bash
# Unit tests + e2e tests
make test

# Unit tests with node debugger
make test-debug

# Unit test with watch and just test one file
# Edit package.json and use for instance
#
# "test:unit": "jest --testPathPattern='apiSpecificationFile.*'",
#
# then
make test-watch 
```

## Quickstart
Capitalize on low hanging fruit to identify a ballpark value added activity to beta test. Override the digital divide with additional clickthroughs from DevOps. Nanotechnology immersion along the information highway will close the loop on focusing solely on the bottom line.

```javascript
	function TasksViewModel() {
        var self = this;
        self.tasks = ko.observableArray();

        self.tasks([
            {
                title: ko.observable('title #1'),
                description: ko.observable('description #1'),
                done: ko.observable(false)
            },
            {
                title: ko.observable('title #2'),
                description: ko.observable('description #2'),
                done: ko.observable(true)
            }
        ]);

        self.beginAdd = function() {
            alert("Add");
        }
        self.beginEdit = function(task) {
            alert("Edit: " + task.title());
        }
        self.remove = function(task) {
            alert("Remove: " + task.title());
        }
        self.markInProgress = function(task) {
            task.done(false);
        }
        self.markDone = function(task) {
            task.done(true);
        }
    }
    ko.applyBindings(new TasksViewModel(), $('#main')[0]);
```
## Note about environment variables and node_modules_custom
We want to be able to build one image and deploy it various environments, using environment variables
to control which resources (URLs, etc) that are used at runtime. The way of referring to environment variables in Nuxt,
is using the `env` property (). However, it's only possible to refer to environment variables set at build time,
not at runtime. Thus, we end up with having to build one docker image for our test environment, one for production,
and so on, which we _don't_ want. We want one docker image that will be deployed to all possible environments,
and use runtime environment variables to configure it. This is according to best practices, see https://12factor.net/config.

We need, however, to use runtime environment variables two different places:

* Environment variables needed inside the Nuxt framework. A Vue component may contain a link that contains
a base URL that should come from an environment variable.
* Environment variables used in `nuxt.config.js` -> `auth` -> `strategies`.

They both need a different solution:
* For the first case, we use the node module `nuxt-env`. With it, we can refer to `this.$env.BASE_URL` in
a Vue component, and it is resolved to the actual runtime contents of the variable `process.env.BASE_URL`.
* For the second case, the code in nuxt.config.js is configuration for Nuxt, and can't use a Nuxt module.

Also, the `nuxt-auth` module uses templates (see `<%=` syntax in 
[plugin.js](source/node_modules_custom/@nuxtjs/auth/lib/module/plugin.js)) that are compiled to strings during
build.

The solution is to modify the `nuxt-auth` module, since we already have modified it by adding a Keycloak auth
provider. (We're using `node_modules_custom/auth` with code from an online PR somewhere instead of just a
dependency on `nuxt-auth`). And we're likely to write our own version in not too far future (see #59).

We have modified `nuxt-auth` by refering to for instance `$BASE_URL$` in `nuxt.config.js`, which is a custom
syntax that is resolved at runtime to process.env.BASE_URL at runtime, similar to how `nuxt-env` does it. The
code for this is mainly in [oauth2.js](source/node_modules_custom/@nuxtjs/auth/lib/schemes/oauth2.js).

Related issue: #6.

## Testing Internet Explorer 11 on Mac
1. Install Virtualbox
2. Download ie11 developer image from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)
3. To access localhost:3333 from the vm, go to 10.0.2.2:3333. This might give issues during login redirect.
If you experience issues, see [Mapping vm localhost to host machine](###Mapping vm localhost to host machine)

### Mapping vm localhost to host machine
If you experience issues during login redirect, try this:
Add the following line to the file *C:\windows\system32\drivers\etc\hosts*:

`10.0.2.2 localhost`

This should map localhost to 10.0.0.2

## Project setup
### Intellij/Webstorm
#### Languagues & Frameworks
Choose ECMAScript 6

#### Code style
* Go to settings->editor->code style->JavaScript->Schemes->Import Scheme->Intellij IDEA code style XML. Choose Javascript_style.xml from the config folder
* Enable the eslint plugin (search for it in settings)
* Enable the prettier plugin

## Style guide
[Git commit standard](https://github.oslo.kommune.no/origodigi/project/blob/master/git-commit-standard.md)
### Components
#### Root element class
SomeComponent.vue:
``` html
<template>
  <div class="SomeComponent">
    ...
  </div>
</template>
```
The root tag in all components should have a css class with the same, capitalized name as the component.
This way we can style the component from a parent without having to wrap it (vue components cannot have classes).
```
<template>
  <SomeComponent/>
</template>

<style>
.SomeComponent {...}
</style>
```

### Css
#### scoped
`<style lange="scss" scoped>`
Use this to make sure our scss does not leak to other parts of the application


### Notes on packages
Remove `"babel-core": "7.0.0-bridge.0"` when `"jest": "24.1.0"` and `"babel-jest": "24.1.0"`
decide to play nice together, i.e. depend on the same babel core dependency.
