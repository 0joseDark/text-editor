#include <QApplication>
#include <QMainWindow>
#include <QTextEdit>
#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QFileDialog>
#include <QMessageBox>
#include <QToolBar>
#include <QKeySequence>
#include <QFile>
#include <QTextStream>

class EditorDeTexto : public QMainWindow {
    Q_OBJECT

public:
    EditorDeTexto() {
        // Configurações iniciais da janela
        setWindowTitle("Editor de Texto");
        resize(600, 400);

        // Criação da caixa de texto principal
        caixaTexto = new QTextEdit(this);
        setCentralWidget(caixaTexto);

        // Criação do menu
        QMenu *menuArquivo = menuBar()->addMenu("Arquivo");

        // Ação para abrir um arquivo
        QAction *acaoAbrir = new QAction("Abrir", this);
        acaoAbrir->setShortcut(QKeySequence("Ctrl+O"));
        connect(acaoAbrir, &QAction::triggered, this, &EditorDeTexto::abrirArquivo);
        menuArquivo->addAction(acaoAbrir);

        // Ação para salvar um arquivo
        QAction *acaoSalvar = new QAction("Salvar", this);
        acaoSalvar->setShortcut(QKeySequence("Ctrl+S"));
        connect(acaoSalvar, &QAction::triggered, this, &EditorDeTexto::salvarArquivo);
        menuArquivo->addAction(acaoSalvar);

        // Separador e ação para sair
        menuArquivo->addSeparator();
        QAction *acaoSair = new QAction("Sair", this);
        acaoSair->setShortcut(QKeySequence("Ctrl+Q"));
        connect(acaoSair, &QAction::triggered, this, &EditorDeTexto::close);
        menuArquivo->addAction(acaoSair);

        // Menu de ajuda
        QMenu *menuAjuda = menuBar()->addMenu("Ajuda");
        QAction *acaoSobre = new QAction("Sobre", this);
        connect(acaoSobre, &QAction::triggered, this, &EditorDeTexto::mostrarSobre);
        menuAjuda->addAction(acaoSobre);

        // Barra de ferramentas com botões
        QToolBar *barraFerramentas = addToolBar("Ferramentas");
        barraFerramentas->addAction(acaoAbrir);
        barraFerramentas->addAction(acaoSalvar);

        // Ação para limpar o texto
        QAction *acaoLimpar = new QAction("Limpar", this);
        connect(acaoLimpar, &QAction::triggered, this, &EditorDeTexto::limparTexto);
        barraFerramentas->addAction(acaoLimpar);
    }

private slots:
    // Função para abrir um arquivo e exibir o conteúdo na caixa de texto
    void abrirArquivo() {
        QString nomeArquivo = QFileDialog::getOpenFileName(this, "Abrir Arquivo", "", "Text Files (*.txt);;All Files (*)");
        if (!nomeArquivo.isEmpty()) {
            QFile arquivo(nomeArquivo);
            if (arquivo.open(QIODevice::ReadOnly | QIODevice::Text)) {
                QTextStream entrada(&arquivo);
                caixaTexto->setText(entrada.readAll());
                arquivo.close();
            } else {
                QMessageBox::warning(this, "Erro", "Não foi possível abrir o arquivo.");
            }
        }
    }

    // Função para salvar o conteúdo da caixa de texto em um arquivo
    void salvarArquivo() {
        QString nomeArquivo = QFileDialog::getSaveFileName(this, "Salvar Arquivo", "", "Text Files (*.txt);;All Files (*)");
        if (!nomeArquivo.isEmpty()) {
            QFile arquivo(nomeArquivo);
            if (arquivo.open(QIODevice::WriteOnly | QIODevice::Text)) {
                QTextStream saida(&arquivo);
                saida << caixaTexto->toPlainText();
                arquivo.close();
                QMessageBox::information(this, "Salvar", "Arquivo salvo com sucesso!");
            } else {
                QMessageBox::warning(this, "Erro", "Não foi possível salvar o arquivo.");
            }
        }
    }

    // Função para limpar o conteúdo da caixa de texto
    void limparTexto() {
        caixaTexto->clear();
    }

    // Função para mostrar informações sobre o editor
    void mostrarSobre() {
        QMessageBox::about(this, "Sobre", "Editor de Texto em C++\nDesenvolvido com Qt");
    }

private:
    QTextEdit *caixaTexto;  // Área de edição de texto
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    EditorDeTexto editor;
    editor.show();

    return app.exec();
}
