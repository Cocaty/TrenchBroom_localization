// P2-D3B-B01-T3: 独立 QTranslator 离线 QM 查询工具（不启动 TrenchBroom）
#include <QCoreApplication>
#include <QTranslator>
#include <QString>
#include <QByteArray>
#include <QFile>
#include <iostream>
#include <vector>

struct Entry { const char* id; const char* context; const char* source; const char* expected; };

int main(int argc, char** argv)
{
    QCoreApplication app(argc, argv);
    if (argc < 2) { std::cerr << "usage: verifier <qm path>\n"; return 2; }
    QTranslator tr;
    if (!tr.load(QString::fromLocal8Bit(argv[1]))) { std::cerr << "QTranslator::load failed\n"; return 3; }

    const std::vector<Entry> entries = {
        {"bcf80284ebf3", "QObject", "New Document", "\xe6\x96\xb0\xe5\xbb\xba\xe6\x96\x87\xe6\xa1\xa3"},
        {"0843baa95d90", "QObject", "Open Document...", "\xe6\x89\x93\xe5\xbc\x80\xe6\x96\x87\xe6\xa1\xa3..."},
        {"08c86abe1b99", "QObject", "Save Document", "\xe4\xbf\x9d\xe5\xad\x98\xe6\x96\x87\xe6\xa1\xa3"},
        {"c13f05ee9b4e", "QObject", "Save Document as...", "\xe6\x96\x87\xe6\xa1\xa3\xe5\x8f\xa6\xe5\xad\x98\xe4\xb8\xba..."},
        {"e7c5ab696447", "QObject", "Wavefront OBJ...", "Wavefront OBJ..."},
        {"88c5a8202a53", "QObject", "Map...", "\xe5\x9c\xb0\xe5\x9b\xbe\xe6\x96\x87\xe4\xbb\xb6..."},
        {"8626a59ed64f", "QObject", "Exports the current map to a .map file. Layers marked Omit From Export will be omitted.",
         "\xe5\xb0\x86\xe5\xbd\x93\xe5\x89\x8d\xe5\x9c\xb0\xe5\x9b\xbe\xe5\xaf\xbc\xe5\x87\xba\xe4\xb8\xba .map \xe6\x96\x87\xe4\xbb\xb6\xe3\x80\x82\xe6\xa0\x87\xe8\xae\xb0\xe4\xb8\xba\xe2\x80\x9c\xe4\xb8\x8d\xe5\x8f\x82\xe4\xb8\x8e\xe5\xaf\xbc\xe5\x87\xba\xe2\x80\x9d\xe7\x9a\x84\xe5\x9b\xbe\xe5\xb1\x82\xe5\xb0\x86\xe8\xa2\xab\xe5\xbf\xbd\xe7\x95\xa5\xe3\x80\x82"},
        {"c87e891f3904", "QObject", "Load Point File...", "\xe5\x8a\xa0\xe8\xbd\xbd\xe7\x82\xb9\xe8\xbd\xa8\xe8\xbf\xb9\xe6\x96\x87\xe4\xbb\xb6..."},
        {"fe79d727b01f", "QObject", "Reload Point File", "\xe9\x87\x8d\xe6\x96\xb0\xe5\x8a\xa0\xe8\xbd\xbd\xe7\x82\xb9\xe8\xbd\xa8\xe8\xbf\xb9\xe6\x96\x87\xe4\xbb\xb6"},
        {"d4365ad643a4", "QObject", "Unload Point File", "\xe5\x8d\xb8\xe8\xbd\xbd\xe7\x82\xb9\xe8\xbd\xa8\xe8\xbf\xb9\xe6\x96\x87\xe4\xbb\xb6"},
        {"c18158cfc475", "QObject", "Load Portal File...", "\xe5\x8a\xa0\xe8\xbd\xbd BSP \xe9\x97\xa8\xe6\x88\xb7\xe6\x96\x87\xe4\xbb\xb6..."},
        {"8c049a323d0f", "QObject", "Reload Portal File", "\xe9\x87\x8d\xe6\x96\xb0\xe5\x8a\xa0\xe8\xbd\xbd BSP \xe9\x97\xa8\xe6\x88\xb7\xe6\x96\x87\xe4\xbb\xb6"},
        {"92939021173f", "QObject", "Unload Portal File", "\xe5\x8d\xb8\xe8\xbd\xbd BSP \xe9\x97\xa8\xe6\x88\xb7\xe6\x96\x87\xe4\xbb\xb6"},
        {"3dab7bfca406", "QObject", "Reload Material Collections", "\xe9\x87\x8d\xe6\x96\xb0\xe5\x8a\xa0\xe8\xbd\xbd\xe6\x9d\x90\xe8\xb4\xa8\xe9\x9b\x86\xe5\x90\x88"},
        {"1e1111c64470", "QObject", "Reload Entity Definitions", "\xe9\x87\x8d\xe6\x96\xb0\xe5\x8a\xa0\xe8\xbd\xbd\xe5\xae\x9e\xe4\xbd\x93\xe5\xae\x9a\xe4\xb9\x89"},
        {"e6acb688ec6e", "QObject", "Revert Document", "\xe8\xbf\x98\xe5\x8e\x9f\xe6\x96\x87\xe6\xa1\xa3"},
        {"d82719c1af53", "QObject", "Discards any unsaved changes and reloads the map file.",
         "\xe6\x94\xbe\xe5\xbc\x83\xe6\x89\x80\xe6\x9c\x89\xe6\x9c\xaa\xe4\xbf\x9d\xe5\xad\x98\xe7\x9a\x84\xe6\x9b\xb4\xe6\x94\xb9\xef\xbc\x8c\xe5\xb9\xb6\xe9\x87\x8d\xe6\x96\xb0\xe5\x8a\xa0\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9b\xbe\xe6\x96\x87\xe4\xbb\xb6\xe3\x80\x82"},
        {"aa1646cea36e", "QObject", "Close Document", "\xe5\x85\xb3\xe9\x97\xad\xe6\x96\x87\xe6\xa1\xa3"},
    };
    std::cout << "message_id,context,source,expected,QM_lookup_result,comparison\n";
    int pass = 0;
    for (const auto& e : entries) {
        const QString actual = tr.translate(QString::fromUtf8(e.context), QString::fromUtf8(e.source));
        const QByteArray a = actual.toUtf8();
        const bool ok = (a == QByteArray(e.expected));
        if (ok) ++pass;
        std::cout << e.id << ",\"" << e.context << "\",\"" << e.source << "\",\""
                  << e.expected << "\",\"" << a.constData() << "\","
                  << (ok ? "PASS" : "FAIL") << "\n";
    }
    std::cerr << "QTranslator lookup: " << pass << "/" << entries.size() << " passed\n";
    return pass == static_cast<int>(entries.size()) ? 0 : 1;
}
