(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{1177:function(e,t,r){"use strict";r.d(t,"a",(function(){return n}));r(33),r(13),r(16);var n=function(e){var t=Object.keys(e).filter((function(t){return void 0!==e[t]})).map((function(t){return encodeURIComponent(t)+"="+encodeURIComponent(e[t])})).join("&");return"".concat("https://api.logo.com","/api/v2/images?").concat(t)}},1180:function(e,t,r){"use strict";r.r(t);var n=r(46),o=r(1),c=r(3),l=(r(19),r(167),r(23),r(73),r(74),r(25),r(102),r(33),r(47),r(45),r(38),r(40),r(39),r(1230)),d=r(337),f=r(123),content=r(100),h=r(176),v=r(1615),m=r(126),w=r(1177),k=r(12),y={components:{Watermark:d.a,Skeleton:f.a},mixins:[Object(content.d)(["data/call-to-actions","data/error-toasts"],!0)],props:{showWatermark:{type:Boolean,default:!1},canvasClass:{type:String,default:""},canvasStyle:{type:String,default:""},exportWidth:{type:Number,default:1500},background:{type:String,default:"transparent"},showDownload:{type:Boolean,default:!1},cover:{type:Boolean,default:!1},mockup:{type:[Object],required:!0},logo:{type:[Object],required:!0},showLoader:{type:Boolean,default:!0},loaderClass:{type:String,default:"w-full h-full"},loaderStyle:{type:Object,default:null}},data:function(){return{dataUri:null,logoElement:null,canvas:null,id:Math.round(1e4*Math.random()).toString(),mockupWidth:null,mockupHeight:null,exporting:!1,loadedMockup:null,logoSvg:null,rendered:!1,defaultSvgAttributes:{xmlns:"http://www.w3.org/2000/svg",version:"1.1","xmlns:xlink":"http://www.w3.org/1999/xlink","xmlns:svgjs":"http://svgjs.com/svgjs"}}},computed:{loading:function(){return!this.rendered},iconOnlyUrl:function(){return Object(w.a)({logo:this.logo.id,template:"icon-only",fit:"contain",background:"transparent",margins:0,u:this.logo.updated_at,format:"webp",quality:60})},logoWhiteUrl:function(){return Object(w.a)({logo:this.logo.id,primary:"#ffffff",background:"transparent",secondary:"#ffffff",accent:"#ffffff",tertiary:"#ffffff",quaternary:"#000000",margins:0,u:this.logo.updated_at,fit:"contain",format:"webp",quality:60})},logoBlackUrl:function(){return Object(w.a)({logo:this.logo.id,primary:"#000000",background:"transparent",secondary:"#000000",accent:"#000000",tertiary:"#000000",quaternary:"#ffffff",margins:0,u:this.logo.updated_at,fit:"contain",format:"webp",quality:60})},overrides:function(){var e,t;if("string"==typeof this.logo)return{};var r=this.logo.assets.wordmark_fonts[0],n=this.logo.assets.slogan_fonts,o=n.length>0?n[0]:null,l=o?o.id:null,d=o?o.name:null,f=null!==(e=this.logo.assets.palette)&&void 0!==e?e:this.logo.assets.palettes[0];return t={"image.logo":!0,"image.icon_only":!0,"palette.primary":f.primary,"palette.secondary":f.secondary,"palette.tertiary":f.tertiary,"palette.quaternary":f.quaternary,"palette.accent":f.accent},Object(c.a)(t,"image.icon_only",this.iconOnlyUrl),Object(c.a)(t,"palette.background",f.background),Object(c.a)(t,"colors.hex.background",f.background),Object(c.a)(t,"colors.hex.primary",f.primary),Object(c.a)(t,"colors.hex.secondary",f.secondary),Object(c.a)(t,"colors.hex.tertiary",f.tertiary),Object(c.a)(t,"colors.hex.quaternary",f.quaternary),Object(c.a)(t,"colors.hex.accent",f.accent),Object(c.a)(t,"font.wordmark.id",r.id),Object(c.a)(t,"font.wordmark.name",r.name),Object(c.a)(t,"font.slogan.id",l),Object(c.a)(t,"font.slogan.name",d),Object(c.a)(t,"image.logo_white",this.logoWhiteUrl),Object(c.a)(t,"image.logo_black",this.logoBlackUrl),t},logoIsURL:function(){return this.logo.startsWith("http")}},watch:{mockup:function(){this.loadAndRenderCanvas()},logo:function(){this.loadAndRenderCanvas()},background:function(e){this.canvas.backgroundColor=e}},mounted:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(e.$refs.svg){t.next=2;break}return t.abrupt("return");case 2:try{e.canvas=new v.fabric.StaticCanvas(e.id)}catch(e){}return t.next=5,e.loadAndRenderCanvas();case 5:k.a.$emit(k.b.EditorHideLoader);case 6:case"end":return t.stop()}}),t)})))()},beforeDestroy:function(){try{if(this.$refs.canvas)this.$refs.canvas.width=1,this.$refs.canvas.height=1,this.$refs.canvas.getContext("2d").clearRect(0,0,1,1);this.canvas&&(this.canvas.setDimensions({width:1,height:1}),this.canvas.dispose())}catch(e){console.error("Failed to dispose of canvas: ".concat(e))}},methods:{exportMockup:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){var r,n;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(!e.exporting){t.next=2;break}return t.abrupt("return");case 2:return e.exporting=!0,t.next=5,e.canvas.requestRenderAll();case 5:try{r=e.exportWidth/e.canvas.getWidth(),n=e.canvas.toDataURL({multiplier:r}),Object(l.b)({data:n,filename:e.loadedMockup.name+".png"})}catch(t){e.$logger.error(t),e.$fetchState.pending||e.$toast.error(e.page["error-toasts"].download_failed)}finally{e.exporting=!1}case 6:case"end":return t.stop()}}),t)})))()},loadAndRenderCanvas:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(t.prev=0,e.loadedMockup){t.next=12;break}if(!e.mockup.id){t.next=8;break}return t.next=5,e.fetchFromAPI();case 5:e.loadedMockup=t.sent,t.next=12;break;case 8:return t.next=10,r(1619)("./".concat(e.mockup.name));case 10:n=t.sent,e.loadedMockup=n.default;case 12:return e.canvas.setDimensions({width:e.loadedMockup.width,height:e.loadedMockup.height}),t.next=15,e.render();case 15:e.rendered=!0,e.$emit("rendered"),t.next=22;break;case 19:t.prev=19,t.t0=t.catch(0),console.log("e",t.t0);case 22:case"end":return t.stop()}}),t,null,[[0,19]])})))()},render:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){var r,o,c,l,d;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if("object"===Object(n.a)(e.logo)&&e.logo.svg&&(r=Object(h.SVG)().addTo(e.$refs.svg),(o=r.svg(e.logo.svg).findOne("#tight-bounds").children()[0]).attr(e.defaultSvgAttributes),e.logoSvg=o.svg(),r.remove()),e.loadedMockup.overrides)for(c in e.loadedMockup.overrides)l=e.loadedMockup.overrides[c],(d=e.overrides[l])&&(e.loadedMockup[c]=d);return e.loadedMockup.objects.map((function(t){if(t.overrides)for(var r in t.overrides)if(e.overrides[t.overrides[r]]&&(t[r]=e.overrides[t.overrides[r]],t.overrides[r].includes("image"))){var n=t.width*t.scaleX,o=t.height*t.scaleY;if(t.width=n,t.height=o,t.scaleX=1,t.scaleY=1,"string"!=typeof e.overrides[t.overrides[r]]&&e.logoSvg)try{var c=Object(h.SVG)().addTo(e.$refs.svg).size(t.width,t.height);c.attr(e.defaultSvgAttributes);var l=c.group();l.svg(e.logoSvg);var d=l.first();d.width(t.width);var f=d.attr(),v=f.height,m=f.width;v>t.height&&d.height(t.height),m>t.width&&d.width(t.width),d.center(t.width/2,t.height/2),d.attr({viewbox:"0 0 ".concat(t.width," ").concat(t.height)}),t.src="data:image/svg+xml;base64,"+btoa(c.svg()),c.remove()}catch(e){console.log("e",e)}else t.src+="&width=".concat(n,"&height=").concat(o)}})),t.next=5,e.loadAllFonts(e.loadedMockup.objects);case 5:return t.next=7,new Promise((function(t){try{e.canvas.loadFromJSON(e.loadedMockup,(function(){e.canvas.getObjects().forEach((function(e){if("i-text"===e.type){var t=e.fontFamily.replace("Regular","");e.set("fontFamily",t),e.fixedWidth&&e.set("width",e.fixedWidth)}})),e.canvas.setBackgroundColor(e.loadedMockup.background,(function(){e.canvas.renderAll(),e.dataUri=e.canvas.toDataURL({}),t()}))}))}catch(e){}}));case 7:case"end":return t.stop()}}),t)})))()},loadAllFonts:function(e){return Object(o.a)(regeneratorRuntime.mark((function t(){var r;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return r=e.map(function(){var e=Object(o.a)(regeneratorRuntime.mark((function e(t){var r,n;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!t.fontId){e.next=4;break}return r="https://cdn.logo.com/assets/fonts/".concat(t.fontId,".ttf"),n=t.fontFamily.replace("Regular",""),e.abrupt("return",Object(m.a)(n,r,{style:t.fontStyle,weight:t.fontWeight}));case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()),t.next=3,Promise.all(r);case 3:case"end":return t.stop()}}),t)})))()},fetchFromAPI:function(){var e=this;return Object(o.a)(regeneratorRuntime.mark((function t(){var r,data,n,canvas,o,c,l,d,f;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,e.$api.get("/api/v2/stitch/mockups/"+e.mockup.id,{params:{relations:"canvas.pages"}});case 3:return r=t.sent,data=r.data,n=data.name,canvas=data.canvas,o=canvas.pages[0],c=o.background,l=o.objects,d=o.overrides,f={height:canvas.height,width:canvas.width,background:c,objects:l,name:n,overrides:d},t.abrupt("return",f);case 11:t.prev=11,t.t0=t.catch(0),console.error(t.t0);case 14:case"end":return t.stop()}}),t,null,[[0,11]])})))()}}},x=y,j=(r(1620),r(8)),component=Object(j.a)(x,(function(){var e=this,t=e._self._c;return t("div",{ref:"container",staticClass:"w-full",on:{contextmenu:function(e){e.preventDefault()}}},[e.loading&&e.showLoader?t("Skeleton",{class:e.loaderClass,style:e.loaderStyle}):e._e(),e._v(" "),t("div",{directives:[{name:"show",rawName:"v-show",value:!e.loading,expression:"!loading"}],staticClass:"w-full h-full"},[e.showWatermark?t("div",{staticClass:"relative"},[t("Watermark",{attrs:{background:e.background}})],1):e._e(),e._v(" "),t("canvas",{ref:"canvas",class:e.canvasClass?e.canvasClass:["w-full h-full",{"object-cover":e.cover}],style:e.canvasStyle,attrs:{id:e.id}}),e._v(" "),t("div",{ref:"svg",attrs:{id:"svg"}})]),e._v(" "),e.showDownload?t("footer",{staticClass:"p-4 text-center"},[e.$fetchState.pending&&e.showLoader?t("Skeleton",{staticClass:"w-40 h-10 mx-auto"}):t("button",{staticClass:"btn btn-secondary w-full button-width",attrs:{type:"button",disabled:e.exporting,loading:e.exporting},on:{click:function(t){return e.exportMockup(e.mockup)}}},[e._v("\n      "+e._s(e.page["call-to-actions"].download)+"\n    ")])],1):e._e()],1)}),[],!1,null,"6a52f484",null);t.default=component.exports},1230:function(e,t,r){"use strict";r.d(t,"b",(function(){return c})),r.d(t,"d",(function(){return f})),r.d(t,"c",(function(){return v})),r.d(t,"a",(function(){return m}));var n=r(31),o=r(1);r(19),r(137),r(49),r(25);function c(e){var data=e.data,t=e.filename,a=document.createElement("a");a.href=data,a.style="display: none",a.download=t,document.body.appendChild(a),a.click(),document.body.removeChild(a)}function l(e){return d.apply(this,arguments)}function d(){return(d=Object(o.a)(regeneratorRuntime.mark((function e(t){var r,n,o,data;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=t.$api,n=t.url,e.next=3,r.get(n,{responseType:"arraybuffer"});case 3:return o=e.sent,data=o.data,e.abrupt("return",URL.createObjectURL(new Blob([data])));case 6:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function f(e){return h.apply(this,arguments)}function h(){return(h=Object(o.a)(regeneratorRuntime.mark((function e(t){var r,n,o;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=t.$api,n=t.url,o=t.filename,e.next=3,l({$api:r,url:n});case 3:c({data:e.sent,filename:o});case 5:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function v(e){var t=e.format,r=e.formats,o=void 0===r?{}:r;return t||Object(n.a)(Object.entries(o)[0],1)[0]}function m(e,t){var r=e.name.toLowerCase().split(" ").join("-");return"".concat(r,".").concat(t)}},1481:function(e,t,r){var content=r(1621);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,r(94).default)("30991596",content,!0,{sourceMap:!1})},1616:function(e,t){},1617:function(e,t){},1618:function(e,t){},1619:function(e,t,r){var map={"./":[1179,129],"./business-card-1":[1570,164],"./business-card-1.js":[1570,164],"./collage-2":[1571,165],"./collage-2.js":[1571,165],"./collage-3":[1572,166],"./collage-3.js":[1572,166],"./collage-4":[1573,173],"./collage-4.js":[1573,173],"./google-ad-1":[1574,167],"./google-ad-1.js":[1574,167],"./greeting-card-1":[1575,168],"./greeting-card-1.js":[1575,168],"./greeting-card-2":[1576,169],"./greeting-card-2.js":[1576,169],"./index":[1179,129],"./index.js":[1179,129],"./iphone-mockup-1":[1577,170],"./iphone-mockup-1.js":[1577,170],"./pizza-box-1":[1578,171],"./pizza-box-1.js":[1578,171],"./t-shirt-2":[1579,172],"./t-shirt-2.js":[1579,172]};function n(e){if(!r.o(map,e))return Promise.resolve().then((function(){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}));var t=map[e],n=t[0];return r.e(t[1]).then((function(){return r(n)}))}n.keys=function(){return Object.keys(map)},n.id=1619,e.exports=n},1620:function(e,t,r){"use strict";r(1481)},1621:function(e,t,r){var n=r(93)((function(i){return i[1]}));n.push([e.i,".button-width[data-v-6a52f484]{max-width:10rem}",""]),n.locals={},e.exports=n}}]);
//# sourceMappingURL=e1fa0ce.js.map