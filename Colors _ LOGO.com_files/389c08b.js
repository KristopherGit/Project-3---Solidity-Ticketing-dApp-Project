(window.webpackJsonp=window.webpackJsonp||[]).push([[137,113],{1176:function(e,t,r){"use strict";var n=r(113);t.a={filters:{render:n.a},methods:{render:function(e){return this.$options.filters.render(e,this.ctx||this._self)}}}},1189:function(e,t){e.exports={fontFamily:"Inter, sans-serif"}},1196:function(e,t,r){"use strict";var n={components:{Skeleton:r(123).a},props:{title:{type:String,default:""},loading:{type:Boolean,default:!1}}},o=r(8),component=Object(o.a)(n,(function(){var e=this,t=e._self._c;return t("div",[e.loading?t("Skeleton",{staticClass:"h-6 w-full mb-2.5"}):t("h5",{staticClass:"border-b-2 border-gray-300 text-gray-600 pb-1 mb-2 font-bold"},[e._v("\n    "+e._s(e.title)+"\n    "),e._t("default")],2)],1)}),[],!1,null,null,null);t.a=component.exports},1244:function(e,t,r){var content=r(1288);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,r(94).default)("5d344767",content,!0,{sourceMap:!1})},1260:function(e,t,r){r(86);var n=r(1189).fontFamily,o=r(1354),l=o.transitions,c=o.typography,d=o.buttons,f=o.toasts,base=o.base;e.exports={important:!0,theme:{fontFamily:{heading:n,text:n},screens:{"2xs":"390px",xs:"448px",sm:"640px",md:"768px","md-lg":"900px",lg:"1024px",xl:"1280px","2xl":"1440px","3xl":"1600px"},extend:{fontSize:{xxs:"0.625rem",xs:"0.75rem","3xl":"1.75rem","4xl":"2.5rem","6xl":"4rem"},colors:{upgrade:"#F3BF4C",light:"#f4f7fd",dark:"#110922","dark-blue":"#02193c","primary-blue":"#1890ff","logo-blue":"#3F83F8",enterprise:{primary:"var(--color-enterprise-primary, #1890ff)",secondary:"var(--color-enterprise-secondary, #26D17F)"}},maxWidth:{"2xs":"15rem"},zIndex:{1:"1",1e3:"1000",9998:"9998",9999:"9999",1e4:"10000"},inset:{"1/2":"50%"},rotate:{225:"225deg"},boxShadow:{primary:"0 0 0 3px var(--color-enterprise-primary)",secondary:"0 0 0 3px var(--color-enterprise-secondary)","inner-x":"inset 0px 0px 75px 50px rgba(0,0,0,0.5)"},scale:{"-1":"-1"}}},variants:{zIndex:["responsive","hover"],borderRadius:["responsive","first","last"]},plugins:[r(1355),l,c,d,f,base],corePlugins:{container:!1},purge:{content:["./pages/**/*.vue","./layouts/**/*.vue","./components/**/*.vue","./content/**/*.md","./content/**/*.json"],whitelist:["html","body","has-navbar-fixed-top","nuxt-link-exact-active","nuxt-progress"],whitelistPatternsChildren:[/svg-inline--fa/,/__layout/,/__nuxt/],defaultExtractor:function(content){return content.match(/[\w-/.:]*[\w-/]/g)||[]}},future:{removeDeprecatedGapUtilities:!0,purgeLayersByDefault:!0,standardFontWeights:!0,defaultLineHeights:!0}}},1282:function(e,t,r){"use strict";r(16),r(15),r(17),r(18);var n=r(1),o=r(20),l=r(3),c=(r(19),r(167),r(33),r(226),r(40),r(23),r(39),r(51),r(224),r(13),r(49),r(124)),d=r.n(c),f=r(12),y=r(338),content=r(100),h=r(30);function w(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}var m={components:{ArrowRight:d.a},mixins:[Object(content.d)(["data/call-to-actions"],!0)],props:{keywordedPhrases:{type:Array,default:function(){return[]}},search:{type:String,default:null},disabled:{type:Boolean,default:!1},showWordark:{type:Boolean,default:!0},showSlogan:{type:Boolean,default:!0},pagination:{type:Number,default:8}},data:function(){return{phrases:[],limit:8}},computed:function(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?w(Object(source),!0).forEach((function(t){Object(l.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):w(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}({flattenedKeywords:function(){var e=(this.phrases||[]).map((function(e){return e.words.map((function(e){return e.synonyms}))})),t=Object(y.a)([].concat(Object(o.a)(this.wordmark),Object(o.a)(this.slogan),Object(o.a)(e)),2);return Object(o.a)(new Set(t))},displayKeywords:function(){return this.flattenedKeywords.slice(0,this.limit)},wordmark:function(){return this.showWordark?this.convertInputToArray(this.session.wordmark):[]},slogan:function(){return this.showSlogan?this.convertInputToArray(this.session.slogan):[]}},Object(h.e)(["session"])),watch:{keywordedPhrases:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[];this.phrases=e||[]}},created:function(){this.limit=this.pagination},mounted:function(){this.search?this.fetchKeywords(this.search):this.phrases=this.keywordedPhrases||[],f.a.$on(f.b.AppWordCloudUpdated,this.fetchKeywords)},beforeDestroy:function(){f.a.$off(f.b.AppWordCloudUpdated,this.fetchKeywords)},methods:{fetchKeywords:function(){var e=arguments,t=this;return Object(n.a)(regeneratorRuntime.mark((function r(){var n,o,data;return regeneratorRuntime.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:if(n=e.length>0&&void 0!==e[0]?e[0]:""){r.next=3;break}return r.abrupt("return");case 3:return r.prev=3,r.next=6,t.$api.get("https://kwd.logo.com",{params:{phrases:n.trim()}});case 6:o=r.sent,data=o.data,t.phrases=data.phrases,r.next=14;break;case 11:r.prev=11,r.t0=r.catch(3),t.$sentry.captureException(r.t0);case 14:case"end":return r.stop()}}),r,null,[[3,11]])})))()},convertInputToArray:function(input){return input?input.toLowerCase().split(" ").filter(Boolean):[]}}},v=m,O=r(8),component=Object(O.a)(v,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"flex flex-wrap gap-2",class:{"opacity-50 cursor-not-allowed":e.disabled}},[e._l(e.displayKeywords,(function(r){return t("span",{key:r,staticClass:"btn cursor-pointer btn-naked text-sm rounded-full",class:{"pointer-events-none opacity-50":e.disabled},attrs:{type:"button"},on:{click:function(t){return e.$emit("select",r)}}},[e._v("\n    "+e._s(r)+"\n  ")])})),e._v(" "),e.limit<e.flattenedKeywords.length?t("span",{staticClass:"btn cursor-pointer mx-0.5 mb-1 text-xs font-bold text-green-500",class:{"pointer-events-none opacity-50":e.disabled},attrs:{type:"button"},on:{click:function(t){e.limit=e.limit+e.pagination}}},[e._v("\n    "+e._s(e.page.view_more)+"\n\n    "),t("ArrowRight",{staticClass:"w-3.5 h-3.5 ml-1 mb-px"})],1):e._e()],2)}),[],!1,null,null,null);t.a=component.exports},1287:function(e,t,r){"use strict";r(1244)},1288:function(e,t,r){var n=r(93)((function(i){return i[1]}));n.push([e.i,".pill.active[data-v-5616d963]{transform:translateX(calc(100% - .25rem))}",""]),n.locals={},e.exports=n},1304:function(e,t,r){"use strict";var n=r(173),o=r.n(n),l=r(168),c=r(123),d={components:{InformationCircle:o.a,Tippy:l.a,Skeleton:c.a},props:{showLabels:{type:Boolean,default:!1},disabled:{type:Boolean,default:!1},layout:{type:String,default:"right"},description:{type:String,default:""},active:{type:Boolean,default:!1},tippy:{type:String,default:""},label:{type:String,default:""},showLabelLoader:{type:Boolean,default:!1},labelLoaderHeight:{type:String,default:"h-4"},labelLoaderWidth:{type:String,default:"w-44"},labelLoaderClass:{type:String,default:""}}},f=(r(1287),r(8)),component=Object(f.a)(d,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"inline-flex items-center gap-3",class:{"pointer-events-none opacity-50":e.disabled,"flex-row-reverse":"left"===e.layout,"w-full":e.tippy}},[t("button",{staticClass:"p-0.5 relative appearance-none inline-flex flex-shrink-0 rounded-full border border-gray-200 cursor-pointer focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500",class:[e.showLabels?"w-16":"w-10"],attrs:{type:"button","aria-pressed":"false","aria-labelledby":"toggleLabel",disabled:e.disabled},on:{click:function(t){return e.$emit("toggle")}}},[t("span",{staticClass:"sr-only"},[e._v("Toggle "+e._s(e.label))]),e._v(" "),t("span",{staticClass:"pill rounded-full shadow ring-0 transition ease-in-out duration-200",class:[{active:e.active},"bg-enterprise-primary",e.showLabels?"h-8 w-8":"h-5 w-5"],attrs:{"aria-hidden":"true"}}),e._v(" "),e.showLabels?t("div",{staticClass:"absolute z-1 p-0.5 inset-0 grid grid-cols-2 items-center text-center leading-none text-xs text-white"},[t("span",{staticClass:"pt-px",class:e.active?"text-gray-300":"text-white"},[e._v("\n        Off\n      ")]),e._v(" "),t("span",{staticClass:"pt-px",class:e.active?"text-white":"text-gray-300"},[e._v("\n        On\n      ")])]):e._e()]),e._v(" "),e.label||e.description?t("label",{staticClass:"relative label w-full mb-0",class:{"pr-5":e.tippy},attrs:{id:"toggleLabel"}},[e.label?t("span",{staticClass:"text-sm font-medium"},[e._v("\n      "+e._s(e.label)+"\n    ")]):e._e(),e._v(" "),e.description?t("span",{staticClass:"text-sm text-gray-500"},[e._v("\n      "+e._s(e.description)+"\n    ")]):e._e(),e._v(" "),t("Tippy",{staticClass:"absolute right-0 top-0 bottom-0 h-full flex items-center leading-none",attrs:{content:e.tippy}},[t("InformationCircle",{staticClass:"inline-block w-4 h-4"})],1)],1):e._e(),e._v(" "),e.showLabelLoader?t("Skeleton",{class:[e.labelLoaderHeight,e.labelLoaderWidth,e.labelLoaderClass]}):e._e()],1)}),[],!1,null,"5616d963",null);t.a=component.exports},1317:function(e,t,r){"use strict";r(167),r(16),r(15),r(13),r(17),r(18);var n=r(3),o=r(355);function l(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}r(14).a.use(o.a);var c={props:{buttonText:{type:String,default:""},buttonTypeClass:{type:String,default:"btn-naked"},tippy:{type:String,default:""},options:{type:Object,default:function(){return{}}}},computed:{tippyOptions:function(){return function(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?l(Object(source),!0).forEach((function(t){Object(n.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):l(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}({animation:"scale",duration:200,arrow:!0,delay:[0,50],arrowType:"sharp",theme:"light",maxWidth:220},this.options)}}},d=c,f=r(8),y={components:{TippyButton:Object(f.a)(d,(function(){var e=this,t=e._self._c;return e.tippy?t("button",{directives:[{name:"tippy",rawName:"v-tippy",value:e.tippyOptions,expression:"tippyOptions"}],staticClass:"btn",class:e.buttonTypeClass,attrs:{content:e.tippy},on:{click:function(t){return e.$emit("click")}}},[e._t("default",(function(){return[e._v("\n    "+e._s(e.buttonText)+"\n  ")]}))],2):t("button",{staticClass:"btn",class:e.buttonTypeClass,on:{click:function(t){return e.$emit("click")}}},[e._t("default",(function(){return[e._v("\n    "+e._s(e.buttonText)+"\n  ")]}))],2)}),[],!1,null,null,null).exports},props:{buttonText:{type:String,default:""},buttonTypeClass:{type:String,default:"btn-naked"},count:{type:Number,default:0},loading:{type:Boolean,default:!1},disabled:{type:Boolean,default:!1},tippy:{type:String,default:""},options:{type:Object,default:function(){return{}}}},data:function(){return{limit:9}},computed:{bubbleText:function(){return this.count>this.limit?"9+":this.count}}},h=Object(f.a)(y,(function(){var e=this,t=e._self._c;return t("TippyButton",{class:e.count?"border-enterprise-primary":"",attrs:{buttonTypeClass:e.buttonTypeClass,loading:e.loading,disabled:e.disabled,tippy:e.tippy,options:e.options},on:{click:function(t){return e.$emit("click")}}},[e._t("default",(function(){return[t("span",[e._v(e._s(e.buttonText))])]})),e._v(" "),e.count?t("div",{staticClass:"bg-enterprise-primary text-white rounded-full absolute top-0 right-0 w-4 h-4 transform translate-x-1 -translate-y-1 flex justify-center items-center"},[t("span",{staticClass:"text-xxs"},[e._v(e._s(e.bubbleText))])]):e._e()],2)}),[],!1,null,null,null);t.a=h.exports},1367:function(e,t,r){"use strict";r(16),r(15),r(13),r(17),r(18);var n=r(3),o=r(12),l=r(30);function c(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}t.a={computed:function(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?c(Object(source),!0).forEach((function(t){Object(n.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):c(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}({value:{get:function(){return this.get},set:function(e){e!==this.value&&(this.set(e),o.a.$emit(o.b.EditorFetchIdeas))}}},Object(l.e)(["editor"])),methods:Object(l.b)({refreshLogos:"app/refreshLogos"})}},1606:function(e,t,r){"use strict";r(47),r(45),r(16),r(15),r(13),r(17),r(18);var n=r(1),o=r(3),l=(r(19),r(30)),c=r(1196),d=r(323),f=r(1304),y=r(334),h=r(1367),w=r(12);function m(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}var v={components:{Lightswitch:f.a,FieldLabel:y.a},mixins:[h.a],data:function(){return{type:"Icon"}},computed:{enabled:function(){return"force-invisible"!==this.value},get:function(){return this.editor.icon_visibility}},methods:function(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?m(Object(source),!0).forEach((function(t){Object(o.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):m(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}({toggle:function(){this.value=this.enabled?"force-invisible":"force-visible",w.a.$emit(w.b.IdeasIconToggled)}},Object(l.d)({set:"editor/SET_ICON_VISIBILITY"}))},O=v,x=r(8),_=Object(x.a)(O,(function(){var e=this,t=e._self._c;return t("div",[t("FieldLabel",{staticClass:"pl-2.5",attrs:{label:"Icons"}}),e._v(" "),t("Lightswitch",{attrs:{layout:"top","show-labels":!0,disabled:!1,active:e.enabled},on:{toggle:e.toggle}})],1)}),[],!1,null,null,null).exports,j=r(20),k=(r(33),r(51),r(1176)),content=r(100),S=r(340),C=r(1282),T=r(1309),I=r.n(T),K=r(1260),P=r.n(K);function D(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function E(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?D(Object(source),!0).forEach((function(t){Object(o.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):D(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var L={components:{FieldMessage:S.a,FieldLabel:y.a,WordCloud:C.a},props:{menuWidth:{type:String,default:"20rem"},menuOffsetPadding:{type:String,default:"1.5rem"}},mixins:[Object(content.d)(["editor/controls/ideas"],!0),k.a,content.b,content.c],data:function(){return{maxCharacters:30,showWordcloud:!1,maxKeywords:3,timeout:null,input:"",fullConfig:null,useMenuOffset:!1,offset:0,showMaxKeywordMessage:!1}},created:function(){this.initKeywords()},mounted:function(){w.a.$on(w.b.IdeasIconToggled,this.onIconToggle),this.fullConfig=I()(P.a)},beforeDestroy:function(){w.a.$off(w.b.IdeasIconToggled,this.onIconToggle)},computed:E(E({iconVisibilty:function(){return this.editor.icon_visibility},keywords:{get:function(){return this.editor.custom_keywords.map((function(text){return{text:text}}))},set:function(e){this.SET_CUSTOM_KEYWORDS(e.map((function(e){return e.text}))),this.iconsEnabled&&this.$emit("generate")}},tagsOptions:function(){return{maxTags:this.maxKeywords,addOnKey:[13,188],tags:this.keywords,placeholder:"",lastKeyword:null}},reachedMaxKeywords:function(){return this.keywords.length===this.maxKeywords},iconsEnabled:function(){return"force-invisible"!==this.iconVisibilty}},Object(l.c)({getKeywords:"session/getKeywords"})),Object(l.e)(["session","editor"])),methods:E({onClickTagInput:function(){this.reachedMaxKeywords&&(this.showMaxKeywordMessage=!0)},convertRemToPixels:function(e){return parseFloat(e)*parseFloat(getComputedStyle(document.documentElement).fontSize)},offsetMenu:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"1rem",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,r=window.innerWidth;if(this.$refs.container&&r>=t){var n=this.convertRemToPixels(this.menuWidth),o=this.$refs.container.getBoundingClientRect(),l=Math.round(o.x),c=Math.round(o.width),d=l+n,f=r-this.convertRemToPixels(e);if(c<n&&d>f)return this.useMenuOffset=!0,f-d}return this.useMenuOffset=!1,0},onIconToggle:function(){0===this.keywords.length&&"force-visible"===this.iconVisibilty&&this.lastKeyword&&(this.showMaxKeywordMessage=!1,this.keywords=[this.lastKeyword])},onTagsChanged:function(e){0===e.length&&1===this.keywords.length&&(this.lastKeyword=this.keywords[0]),e.length>this.keywords.length&&"force-invisible"===this.iconVisibilty&&this.$store.commit("editor/SET_ICON_VISIBILITY","force-visible"),this.keywords=e,this.keywords&&(0===this.keywords.length&&this.$store.commit("editor/SET_ICON_VISIBILITY","force-invisible"),this.keywords.length<this.maxKeywords&&(this.showMaxKeywordMessage=!1)),this.calculateMenuOffset()},initKeywords:function(){this.keywords.length||(this.keywords=Object(j.a)(this.getKeywords).slice(0,3).map((function(text){return{text:text}})))},addKeyword:function(text){this.keywords.length!==this.maxKeywords?(this.keywords=[].concat(Object(j.a)(this.keywords),[{text:text}]),this.focusInput(),this.keywords.length>0&&"force-invisible"===this.iconVisibilty&&(this.$store.commit("editor/SET_ICON_VISIBILITY","force-visible"),w.a.$emit(w.b.EditorFetchIdeas))):this.showMaxKeywordMessage=!0},focusInput:function(){try{document.getElementsByClassName("ti-new-tag-input")[0].focus()}catch(e){console.error(e)}},openWordcloud:function(){clearTimeout(this.timeout),this.calculateMenuOffset(),this.showWordcloud=!0},calculateMenuOffset:function(){this.offset=this.offsetMenu(this.menuOffsetPadding,parseInt(this.fullConfig.theme.screens.sm))},closeWordcloud:function(){var e=this;return Object(n.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return e.showMaxKeywordMessage=!1,t.next=3,e.$nextTick();case 3:e.timeout=setTimeout((function(){return e.showWordcloud=!1}),500);case 4:case"end":return t.stop()}}),t)})))()}},Object(l.d)({SET_CUSTOM_KEYWORDS:"editor/SET_CUSTOM_KEYWORDS"}))},F=L,M=Object(x.a)(F,(function(){var e=this,t=e._self._c;return t("div",{ref:"container"},[t("div",{staticClass:"w-full"},[t("FieldLabel",{staticClass:"pl-0.5",attrs:{label:e.fields.keywords?e.render(e.fields.keywords.label):"",tippy:e.fields.keywords?e.render(e.fields.keywords.tippy):""}}),e._v(" "),t("div",{staticClass:"relative"},[t("div",{on:{click:e.onClickTagInput}},[t("vue-tags-input",e._b({ref:"input",staticClass:"vue-tags-input-small",attrs:{maxlength:e.maxCharacters,"max-tags":e.maxKeywords},on:{"tags-changed":e.onTagsChanged,focus:e.openWordcloud,blur:e.closeWordcloud},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}},"vue-tags-input",e.tagsOptions,!1))],1),e._v(" "),t("transition",{attrs:{name:"dropdown"}},[e.showWordcloud?t("aside",{staticClass:"absolute my-2 max-w-full sm:max-w-none sm:w-80 rounded-md border bg-white border-gray-100 shadow-lg z-10 p-2 overflow-hidden",style:e.useMenuOffset?{transform:"translateX(".concat(e.offset,"px)")}:{},attrs:{tabindex:"0"},on:{focus:e.focusInput}},[t("WordCloud",{attrs:{"keyworded-phrases":e.session.keywordedPhrases,pagination:6},on:{select:e.addKeyword}}),e._v(" "),e.reachedMaxKeywords?t("FieldMessage",{attrs:{"status-message":"You've reached the maximum keywords.","is-success":!1,"is-error":!0}}):e._e()],1):e._e()])],1)],1)])}),[],!1,null,null,null).exports,W=r(488),$=r.n(W),B=r(441),A=r(1317);function R(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function N(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?R(Object(source),!0).forEach((function(t){Object(o.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):R(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var V={components:{Modal:r(169).a,FieldLabel:y.a,FieldMessage:S.a,WordCloud:C.a},props:{active:{type:Boolean,default:!1}},mixins:[Object(content.d)(["editor/controls/ideas"],!0),k.a,content.b,content.c],data:function(){return{maxCharacters:30,showWordcloud:!1,maxKeywords:3,timeout:null,input:""}},created:function(){},mounted:function(){w.a.$on(w.b.IdeasIconToggled,this.onIconToggle),this.initKeywords()},beforeDestroy:function(){w.a.$off(w.b.IdeasIconToggled,this.onIconToggle)},computed:N(N({iconVisibilty:function(){return this.editor.icon_visibility},keywords:{get:function(){return this.editor.custom_keywords.map((function(text){return{text:text}}))},set:function(e){this.SET_CUSTOM_KEYWORDS(e.map((function(e){return e.text}))),this.iconsEnabled&&this.$emit("generate")}},tagsOptions:function(){return{maxTags:this.maxKeywords,addOnKey:[13,188],tags:this.keywords,placeholder:"",lastKeyword:null}},reachedMaxKeywords:function(){return this.keywords.length===this.maxKeywords},iconsEnabled:function(){return"force-invisible"!==this.iconVisibilty}},Object(l.c)({getKeywords:"session/getKeywords"})),Object(l.e)(["session","editor"])),methods:N({handleCloseModal:function(e){e.stopPropagation(),this.$emit("close")},onIconToggle:function(){0===this.keywords.length&&"force-visible"===this.iconVisibilty&&this.lastKeyword&&(this.keywords=[this.lastKeyword])},onTagsChanged:function(e){0===e.length&&1===this.keywords.length&&(this.lastKeyword=this.keywords[0]),e.length>this.keywords.length&&"force-invisible"===this.iconVisibilty&&this.$store.commit("editor/SET_ICON_VISIBILITY","force-visible"),this.keywords=e,this.keywords&&0===this.keywords.length&&this.$store.commit("editor/SET_ICON_VISIBILITY","force-invisible")},initKeywords:function(){this.keywords.length||(this.keywords=Object(j.a)(this.getKeywords).slice(0,3).map((function(text){return{text:text}})))},addKeyword:function(text){this.keywords=[].concat(Object(j.a)(this.keywords),[{text:text}]),this.keywords.length>0&&"force-invisible"===this.iconVisibilty&&(this.$store.commit("editor/SET_ICON_VISIBILITY","force-visible"),w.a.$emit(w.b.EditorFetchIdeas))}},Object(l.d)({SET_CUSTOM_KEYWORDS:"editor/SET_CUSTOM_KEYWORDS"}))},U=Object(x.a)(V,(function(){var e=this,t=e._self._c;return t("div",[t("Modal",{attrs:{"can-close":!0,scope:"icon-keyword",small:!0,active:e.active},on:{close:function(t){return e.$emit("close")}}},[t("div",[t("FieldLabel",{staticClass:"pl-0.5",attrs:{label:e.fields.keywords?e.render(e.fields.keywords.label):"",tippy:e.fields.keywords?e.render(e.fields.keywords.tippy):""}}),e._v(" "),t("div",{staticClass:"relative space-y-4"},[t("div",[t("vue-tags-input",e._b({ref:"input",staticClass:"vue-tags-input-small",class:e.reachedMaxKeywords?"disable-input":"",attrs:{maxlength:e.maxCharacters},on:{"tags-changed":e.onTagsChanged},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}},"vue-tags-input",e.tagsOptions,!1)),e._v(" "),e.reachedMaxKeywords?t("FieldMessage",{attrs:{"status-message":"You've reached the maximum keywords.","is-success":!1,"is-error":!0}}):e._e()],1),e._v(" "),t("WordCloud",{attrs:{"keyworded-phrases":e.session.keywordedPhrases,disabled:e.reachedMaxKeywords,pagination:6},on:{select:e.addKeyword}})],1)],1)])],1)}),[],!1,null,null,null).exports;function Y(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function z(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?Y(Object(source),!0).forEach((function(t){Object(o.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):Y(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var H={components:{FieldLabel:y.a,CountButton:A.a,IconKeywordModal:U},props:{},mixins:[Object(content.d)(["editor/controls/ideas"],!0),k.a,content.c],data:function(){return{iconKeywordOpen:!1}},computed:z(z({keywords:{get:function(){return this.editor.custom_keywords.map((function(text){return{text:text}}))},set:function(e){this.SET_CUSTOM_KEYWORDS(e.map((function(e){return e.text}))),this.iconsEnabled&&this.$emit("generate")}}},Object(l.c)({getKeywords:"session/getKeywords"})),Object(l.e)(["session","editor"]))},G=Object(x.a)(H,(function(){var e=this,t=e._self._c;return t("div",[t("FieldLabel",{staticClass:"pl-0.5",attrs:{label:e.fields.keywords?e.render(e.fields.keywords.label):"",tippy:e.fields.keywords?e.render(e.fields.keywords.tippy):""}}),e._v(" "),t("CountButton",{staticClass:"btn btn-naked text-xs text-black px-4 rounded-full w-full",attrs:{buttonText:e.contentReady?e.page.icon_keywords.button_text:"Keywords",count:e.keywords?e.keywords.length:0},on:{click:function(t){e.iconKeywordOpen=!0}}}),e._v(" "),t("IconKeywordModal",{attrs:{active:e.iconKeywordOpen},on:{close:function(t){e.iconKeywordOpen=!1},generate:function(t){return e.$emit("generate")}}})],1)}),[],!1,null,null,null).exports,J=r(41),X=r(85),Q=r(72),Z=r(32);function ee(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function te(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?ee(Object(source),!0).forEach((function(t){Object(o.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):ee(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var re={components:{ControlTitle:c.a,TextInput:d.a,IconFilter:_,IconKeywords:M,FieldLabel:y.a,RefreshIcon:$.a,FavouriteLogosButton:B.a,IconKeywordButton:G},mixins:[Object(content.d)(["editor/controls/ideas"],!0),k.a,content.b,content.c,content.e],props:{showFieldPrompts:{type:Boolean,default:!0},showFavouriteButton:{type:Boolean,default:!1},useModalMenus:{type:Boolean,default:!1},nameInputsClass:{type:String,default:"w-full flex flex-col gap-4"},businessNameClass:{type:String,default:""},sloganClass:{type:String,default:""},iconFilterClass:{type:String,default:""},iconKeywordsClass:{type:String,default:""},iconKeywordButtonClass:{type:String,default:""},generateButtonClass:{type:String,default:""},favouriteButtonClass:{type:String,default:""}},validations:{wordmark:X.n,slogan:X.l},data:function(){return{disabled:!1}},computed:te(te({wordmark:{get:function(){return this.editor.unvalidated_wordmark},set:function(e){this.SET_UNVALIDATED_WORDMARK(e)}},slogan:{get:function(){return this.editor.unvalidated_slogan},set:function(e){this.SET_UNVALIDATED_SLOGAN(e)}}},Object(l.e)(["session","editor","enterprise"])),Object(l.c)({updating:"editor/loading_overlay_visible",getKeywords:"session/getKeywords"})),mounted:function(){var e=this;return Object(n.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:e.initKeywords(),e.populateTextFields(),e.favoriteLogoFromSession();case 3:case"end":return t.stop()}}),t)})))()},methods:te(te({clearSessionFavoriteLogo:function(){Object(Z.b)().removeItem("logo_to_favorite")},favoriteLogoFromSession:function(){var e=this;return Object(n.a)(regeneratorRuntime.mark((function t(){var r,n,o,l,c,d,f,y;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,r=Object(Z.b)().getItem("logo_to_favorite"),n=Object(J.c)(e.$api),o=n.getUser,t.next=5,o().catch((function(){return null}));case 5:if(l=t.sent,r&&l){t.next=9;break}return e.clearSessionFavoriteLogo(),t.abrupt("return");case 9:if((c=JSON.parse(r)).id===e.$route.query.add_favourite){t.next=13;break}return e.clearSessionFavoriteLogo(),t.abrupt("return");case 13:return d=Object(J.b)(e.$api),f=d.favoriteClientSideLogo,t.next=16,Object(Q.e)(c,e.enterprise.id,f);case 16:y=t.sent,e.addToFavourites(y),t.next=23;break;case 20:t.prev=20,t.t0=t.catch(0),e.$sentry.captureException(t.t0);case 23:return t.prev=23,e.clearSessionFavoriteLogo(),t.finish(23);case 26:case"end":return t.stop()}}),t,null,[[0,20,23,26]])})))()},invalidForm:function(){return this.$invalidInput()},generate:function(){var e=this;return Object(n.a)(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(!e.invalidForm()){t.next=2;break}return t.abrupt("return");case 2:return e.editor.custom_keywords.length&&(r=e.editor.custom_keywords.join(" "),e.SET_UNVALIDATED_KEYWORDS(r),e.setKeywords(r)),e.setWordmark(e.wordmark),e.setSlogan(e.slogan),t.next=7,e.sendSessionToKeyworder();case 7:w.a.$emit(w.b.EditorFetchIdeas),e.editor.current_logo&&e.fetchNewLogoFromState();case 9:case"end":return t.stop()}}),t)})))()},initKeywords:function(){var e=this.getKeywords.join(" ");this.SET_UNVALIDATED_KEYWORDS(e)},populateTextFields:function(){var e=this.session,t=e.wordmark,r=e.slogan;this.$store.commit("editor/SET_UNVALIDATED_WORDMARK",t),this.$store.commit("editor/SET_UNVALIDATED_SLOGAN",r),this.$store.commit("session/setWordmark",t),this.$store.commit("session/setSlogan",r)}},Object(l.b)({sendSessionToKeyworder:"session/sendSessionToKeyworder",fetchNewLogoFromState:"editor/fetchNewLogoFromState",refreshLogos:"app/refreshLogos",addToFavourites:"favourites/addLogo"})),Object(l.d)({SET_UNVALIDATED_KEYWORDS:"editor/SET_UNVALIDATED_KEYWORDS",SET_UNVALIDATED_WORDMARK:"editor/SET_UNVALIDATED_WORDMARK",SET_UNVALIDATED_SLOGAN:"editor/SET_UNVALIDATED_SLOGAN",setKeywords:"session/setKeywords",setWordmark:"session/setWordmark",setSlogan:"session/setSlogan"}))},se=Object(x.a)(re,(function(){var e=this,t=e._self._c;return t("div",{},[e.session.wordmark?e._e():t("ControlTitle",{attrs:{title:e.page.empty_text||""}}),e._v(" "),t("div",{class:[e.nameInputsClass]},[t("TextInput",{staticClass:"w-full sm:w-auto",class:[e.businessNameClass],attrs:{id:e.fields.wordmark?e.fields.wordmark.id:"",required:"",maxlength:"30",label:e.fields.wordmark?e.render(e.fields.wordmark.label):"",placeholder:e.fields.wordmark?e.render(e.fields.wordmark.placeholder):"",prompt:e.showFieldPrompts&&e.fields.wordmark?e.fields.wordmark.prompt:"",status:e.fields.wordmark?e.fields.wordmark.status:"","status-message":e.fields.wordmark?e.fields.wordmark.message:"",tippy:e.fields.wordmark?e.render(e.fields.wordmark.tippy):"","hard-disable":!e.editor.features.includes("wordmark")},on:{enter:e.generate},model:{value:e.wordmark,callback:function(t){e.wordmark="string"==typeof t?t.trim():t},expression:"wordmark"}}),e._v(" "),t("TextInput",{staticClass:"w-full sm:w-auto",class:[e.sloganClass],attrs:{id:e.fields.slogan?e.fields.slogan.id:"",maxlength:"40",label:e.fields.slogan?e.render(e.fields.slogan.label):"",placeholder:e.fields.slogan?e.render(e.fields.slogan.placeholder):"",prompt:e.showFieldPrompts&&e.fields.slogan?e.fields.slogan.prompt:"",status:e.fields.slogan?e.fields.slogan.status:"","status-message":e.fields.slogan?e.fields.slogan.message:"",tippy:e.fields.slogan?e.render(e.fields.slogan.tippy):"","hard-disable":!e.editor.features.includes("slogan")},on:{enter:e.generate},model:{value:e.slogan,callback:function(t){e.slogan="string"==typeof t?t.trim():t},expression:"slogan"}})],1),e._v(" "),t("IconFilter",{class:[e.iconFilterClass]}),e._v(" "),t("IconKeywords",{class:[e.iconKeywordsClass],on:{generate:e.generate}}),e._v(" "),e.useModalMenus?t("IconKeywordButton",{class:[e.iconKeywordButtonClass],on:{generate:e.generate}}):e._e(),e._v(" "),e._t("default"),e._v(" "),t("div",{class:[e.generateButtonClass]},[t("FieldLabel",{staticClass:"pl-0.5",attrs:{label:"&nbsp;"}}),e._v(" "),e.contentReady?t("button",{staticClass:"btn btn-tertiary gap-2 flex-1",attrs:{id:e.buttons.generate.id,type:"button",disabled:e.disabled,loading:e.disabled},on:{click:e.generate}},[t("RefreshIcon",{staticClass:"w-5 h-5"}),e._v("\n\n      "+e._s(e.buttons.generate.text)+"\n    ")],1):e._e()],1),e._v(" "),e.showFavouriteButton?t("div",{class:[e.favouriteButtonClass]},[t("FieldLabel",{staticClass:"pl-0.5",attrs:{label:"&nbsp;"}}),e._v(" "),e.contentReady?t("FavouriteLogosButton",{attrs:{text:e.buttons.favorites.text,disabled:e.disabled},on:{click:function(t){return e.$emit("onFavouriteClick")}}}):e._e()],1):e._e()],2)}),[],!1,null,null,null);t.a=se.exports},488:function(e,t,r){r(16),r(15),r(13),r(17),r(18);var n=r(35),o=r(36),l=["class","staticClass","style","staticStyle","attrs"];function c(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}e.exports={functional:!0,render:function(e,t){var r=t._c,data=(t._v,t.data),d=t.children,f=void 0===d?[]:d,y=data.class,h=data.staticClass,style=data.style,w=data.staticStyle,m=data.attrs,v=void 0===m?{}:m,O=o(data,l);return r("svg",function(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?c(Object(source),!0).forEach((function(t){n(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):c(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}({class:[y,h],style:[style,w],attrs:Object.assign({fill:"currentColor",viewBox:"0 0 20 20"},v)},O),f.concat([r("path",{attrs:{"fill-rule":"evenodd",d:"M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z","clip-rule":"evenodd"}})]))}}}}]);
//# sourceMappingURL=389c08b.js.map