(window.webpackJsonp=window.webpackJsonp||[]).push([[257],{1176:function(e,t,r){"use strict";var n=r(113);t.a={filters:{render:n.a},methods:{render:function(e){return this.$options.filters.render(e,this.ctx||this._self)}}}},1187:function(e,t,r){"use strict";var n=r(1176),o=r(30),c={mixins:[n.a],props:{page:{type:Object,default:function(){return{}}},ctx:{type:Object,default:function(){return null}},align:{type:String,default:"text-center"}},computed:Object(o.e)(["enterprise"])},l=r(8),component=Object(l.a)(c,(function(){var e=this,t=e._self._c;return t("header",{directives:[{name:"show",rawName:"v-show",value:e.page.show_intro,expression:"page.show_intro"}],staticClass:"mb-6",class:e.align},[t("div",{class:{"flex flex-col-reverse sm:flex-row sm:justify-between sm:items-center":e.$slots["header-content"]}},[t("h1",{staticClass:"text-3xl md:text-4xl"},[e._v(e._s(e.render(e.page.title)))]),e._v(" "),e._t("header-content")],2),e._v(" "),e.page.intro_text?t("div",{staticClass:"mb-6 mt-2 article",domProps:{innerHTML:e._s(e.render(e.page.intro_text))}}):e._e()])}),[],!1,null,null,null);t.a=component.exports},1299:function(e,t,r){"use strict";var n={components:{Intro:r(1187).a},props:{page:{type:Object,required:!0}}},o=r(8),component=Object(o.a)(n,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"pb-20 max-w-lg mx-auto mt-20 mx-2"},[t("Intro",{attrs:{page:e.page}}),e._v(" "),e._t("default")],2)}),[],!1,null,null,null);t.a=component.exports},2114:function(e,t,r){"use strict";r.r(t);r(16),r(15),r(13),r(17),r(18);var n=r(3),o=(r(38),r(357)),c=r(1299),content=r(100),l=r(332);function f(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function h(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?f(Object(source),!0).forEach((function(t){Object(n.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):f(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var d={transition:"fade",layout:"auth",components:{LoginForm:o.a,AuthPage:c.a},mixins:[l.a,content.e,Object(content.d)(["auth-pages/login"])],middleware:["requires-no-auth"],methods:{handleAuth:function(){var path=this.$route.query.app_return_path||"/dashboard/latest";this.$router.replace({path:path,query:Object.assign(h({},this.$route.query),{app_return_path:void 0})})},goToRegister:function(){this.$router.push({path:"/register",query:h({},this.$route.query)})}}},m=r(8),component=Object(m.a)(d,(function(){var e=this,t=e._self._c;return t("AuthPage",{attrs:{page:e.page}},[t("LoginForm",{on:{login:e.handleContinue,goToRegister:e.goToRegister}})],1)}),[],!1,null,null,null);t.default=component.exports}}]);
//# sourceMappingURL=828de95.js.map