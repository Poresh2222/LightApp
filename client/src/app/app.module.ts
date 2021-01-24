import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { SharedMaterialModule } from './modules/shared-material.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { StartPageComponent } from './components/start-page/start-page.component';
import { SingupRouteComponent, SingupComponentDialog } from './components/dialog/singup/singup.component';
import { SinginComponent } from './components/dialog/singin/singin.component';
import { BaseComponent } from './components/base/base.component';
import { BasePageComponent } from './components/base-page/base-page.component';
import { SingupFormComponent } from './components/dialog/singup-form/singup-form.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    StartPageComponent,
    SingupRouteComponent,
    SingupComponentDialog,
    SinginComponent,
    BaseComponent,
    BasePageComponent,
    SingupFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedMaterialModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
