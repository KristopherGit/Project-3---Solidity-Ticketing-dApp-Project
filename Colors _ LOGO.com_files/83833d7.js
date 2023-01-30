(window.webpackJsonp=window.webpackJsonp||[]).push([[184,301],{1048:function(t){t.exports=JSON.parse('{"title":"Your business name","intro_text":"<p>For example, our business name is <strong>{{ enterprise.name }}</strong></p>","show_intro":true,"input":{"label":"Enter your business name:","placeholder":"eg. {{ enterprise.name }}","field_name":"business name","id":"wordmark","prompt":"","tippy":""},"button":{"text":"Continue","empty_text":"Continue"},"meta":{"title":"Enter Your Business Name","description":""}}')},1176:function(t,e,n){"use strict";var r=n(113);e.a={filters:{render:r.a},methods:{render:function(t){return this.$options.filters.render(t,this.ctx||this._self)}}}},1187:function(t,e,n){"use strict";var r=n(1176),o=n(30),l={mixins:[r.a],props:{page:{type:Object,default:function(){return{}}},ctx:{type:Object,default:function(){return null}},align:{type:String,default:"text-center"}},computed:Object(o.e)(["enterprise"])},c=n(8),component=Object(c.a)(l,(function(){var t=this,e=t._self._c;return e("header",{directives:[{name:"show",rawName:"v-show",value:t.page.show_intro,expression:"page.show_intro"}],staticClass:"mb-6",class:t.align},[e("div",{class:{"flex flex-col-reverse sm:flex-row sm:justify-between sm:items-center":t.$slots["header-content"]}},[e("h1",{staticClass:"text-3xl md:text-4xl"},[t._v(t._s(t.render(t.page.title)))]),t._v(" "),t._t("header-content")],2),t._v(" "),t.page.intro_text?e("div",{staticClass:"mb-6 mt-2 article",domProps:{innerHTML:t._s(t.render(t.page.intro_text))}}):t._e()])}),[],!1,null,null,null);e.a=component.exports},1221:function(t,e,n){"use strict";var r=n(124),o=n.n(r),l=n(1187),c={components:{ArrowRight:o.a,Intro:l.a},props:{input:{type:[String,Array],default:""},page:{type:Object,default:function(){return{}}},name:{type:String,required:!0},loading:Boolean},beforeDestroy:function(){window.removeEventListener("keypress",this.onKeyPress)},mounted:function(){window.addEventListener("keypress",this.onKeyPress)},computed:{skip:function(){var t;return!(null!==(t=this.input)&&void 0!==t&&t.length)},buttonText:function(){var t,e,n,r;return this.skip?null===(t=this.page)||void 0===t||null===(e=t.button)||void 0===e?void 0:e.empty_text:null===(n=this.page)||void 0===n||null===(r=n.button)||void 0===r?void 0:r.text}},methods:{handleContinue:function(t){this.$emit("continue",t)},onKeyPress:function(t){"Enter"===(null==t?void 0:t.key)&&this.handleContinue()}}},d=n(8),component=Object(d.a)(c,(function(){var t=this,e=t._self._c;return e("section",{staticClass:"mb-auto pt-6 pb-12"},[e("div",{staticClass:"max-w-xl mx-auto"},[e("Intro",{attrs:{page:t.page,align:"text-left"}},[e("button",{staticClass:"btn text-left justify-start -ml-2 sm:ml-2",attrs:{slot:"header-content",type:"button",disabled:t.loading,loading:t.loading},on:{click:t.handleContinue},slot:"header-content"},[t._v("\n        "+t._s(t.buttonText)+"\n\n        "),e("ArrowRight",{staticClass:"w-3.5 h-3.5 ml-1 flex-shrink-0"})],1)]),t._v(" "),t.$slots.default?e("div",{staticClass:"mb-5"},[t._t("default")],2):t._e(),t._v(" "),t._t("button",(function(){return[e("button",{staticClass:"btn btn-primary btn-large w-full",attrs:{type:"button",disabled:t.loading,loading:t.loading},on:{click:t.handleContinue}},[t._v("\n        "+t._s(t.buttonText)+"\n\n        "),e("ArrowRight",{staticClass:"btn-icon-right"})],1)]}))],2)])}),[],!1,null,null,null);e.a=component.exports},1409:function(t,e,n){"use strict";var r=n(1);n(19);e.a=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:0;return{data:function(){return{pageReady:!1,delay:t}},mounted:function(){var t=this;return Object(r.a)(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.$nextTick();case 2:setTimeout((function(){t.pageReady=!0}),t.delay);case 3:case"end":return e.stop()}}),e)})))()}}}},2102:function(t,e,n){"use strict";n.r(e);n(16),n(15),n(13),n(17),n(18);var r=n(1),o=n(3),l=(n(19),n(1176)),c=n(85),d=n(347),m=n(323),content=n(100),f=n(12),h=n(1221),v=n(1409),w=n(30),x=n(1048);function y(object,t){var e=Object.keys(object);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(object);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(object,t).enumerable}))),e.push.apply(e,n)}return e}var k={transition:"fade",layout:"progress",components:{StepPage:h.a,TextInput:m.a},mixins:[l.a,Object(v.a)(),content.e],data:function(){return{page:x,submittingForm:!1,form_error:"",wordmark:""}},computed:function(t){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?y(Object(source),!0).forEach((function(e){Object(o.a)(t,e,source[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(source)):y(Object(source)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(source,e))}))}return t}({placeholder:function(){var t,e;return this.enterprise?this.render(null===(t=this.page)||void 0===t||null===(e=t.input)||void 0===e?void 0:e.placeholder):""},label:function(){var t,e;return this.enterprise?this.render(null===(t=this.page)||void 0===t||null===(e=t.input)||void 0===e?void 0:e.label):""},wordmarkValidationError:function(){var t,e;return Object(d.a)(this.$v.wordmark,null===(t=this.page)||void 0===t||null===(e=t.input)||void 0===e?void 0:e.field_name)},wordmarkValidationStatus:function(){return this.$v.wordmark.$error?"error":null},loading:function(){return this.submittingForm||!this.pageReady}},Object(w.e)(["enterprise"])),validations:{wordmark:c.n},created:function(){this.wordmark=this.$store.state.session.wordmark},mounted:function(){var t;this.wordmark.length>0&&(null===(t=this.$v)||void 0===t||t.$touch());f.a.$emit(f.b.StepSetProgress,15)},methods:{saveWordmark:function(){var t=this;return Object(r.a)(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!t.$invalidInput()&&!t.submittingForm){e.next=2;break}return e.abrupt("return");case 2:t.submittingForm=!0;try{t.wordmark!==t.$store.state.session.wordmark&&(t.$store.commit("session/setWordmark",t.wordmark),t.$store.dispatch("app/refreshLogos")),t.$router.push(t.localePath("/slogan"))}catch(e){t.submittingForm=!1}case 4:case"end":return e.stop()}}),e)})))()}}},_=k,O=n(8),component=Object(O.a)(_,(function(){var t=this,e=t._self._c;return e("StepPage",{attrs:{page:t.page,input:t.wordmark,loading:t.loading,name:"Business Name"},on:{continue:t.saveWordmark}},[e("TextInput",{attrs:{autofocus:"",maxlength:"30","data-hj-whitelist":"",status:t.wordmarkValidationStatus,"status-message":t.wordmarkValidationError,label:t.label,placeholder:t.placeholder,prompt:t.page.input.prompt,disabled:t.loading,"input-styles":"form-input-large"},on:{enter:t.saveWordmark},model:{value:t.wordmark,callback:function(e){t.wordmark=e},expression:"wordmark"}})],1)}),[],!1,null,null,null);e.default=component.exports}}]);
//# sourceMappingURL=83833d7.js.map