# refactor
public class UIInitializer {
    public void initializeUI(Stage primaryStage, Injector injector) {
        primaryStage.setScene(initScene(injector));
        primaryStage.getIcons().addAll(injector.instancesOfType(Image.class));
        primaryStage.setTitle(injector.instance(Pdfsam.class).name());
        primaryStage.setOnCloseRequest(e -> Platform.exit());
    }
}

public void start(Stage primaryStage) {
    this.primaryStage = primaryStage;
    injector = initInjector();
    new UIInitializer().initializeUI(primaryStage, injector);
    primaryStage.show();
    // Other startup logic
}

#modified
#Test
public void testInitializeUI() {
    Stage stage = new Stage();
    Injector injector = initInjector();
    UIInitializer initializer = new UIInitializer();
    initializer.initializeUI(stage, injector);
    assertEquals("PDFsam", stage.getTitle());
    assertNotNull(stage.getScene());
}

